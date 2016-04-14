from NDB.search_report import SearchReport
from NDB.search_result import SearchResult
from NDB.summary_result import SummaryResult
from NDB.html_parser import NDBHtmlParser
from NDB.ndb import NDBBase
import re
import requests
import xlrd
import io


def parse_to_table(text: str) -> list:
    return [t.strip() for t in text.splitlines()]


def parse_csv(table: list) -> list:
    result = []
    headers = table[0].split(',')

    for elem in table[1:]:
        before = 0
        last = 0
        record = {}
        open_quotes = False
        values = elem.split(',')
        values_len = len(values)

        for header in headers:
            for i in range(last, values_len):
                if '"' in values[i]:
                    if not open_quotes:
                        before = i
                        open_quotes = True
                    else:
                        record[header] = ",".join(values[before:i+1]).replace('"', '')
                        open_quotes = False
                        last = i+1
                        break
                elif not open_quotes:
                    record[header] = values[i]
                    last = i+1
                    break

        result.append(record)

    return result


def parse_xls(file: io.BytesIO) -> list:
    result = []
    try:
        book = xlrd.open_workbook(file_contents=file.read())
        sheet = book.sheet_by_index(0)
        headers = sheet.row_values(0)

        for row in range(1, sheet.nrows):
            record = dict(zip(headers, sheet.row_values(row)))
            result.append(SearchReport(record))
    except TypeError:
        pass

    return result


def parse_advanced_search_report(text: str) -> SearchResult:
    result = SearchResult()

    raw_table = parse_to_table(text)
    count = raw_table[1].rpartition(': ')[-1]
    report = parse_csv(raw_table[2:])

    try:
        result.set_count(int(count))
    except (TypeError, ValueError, OverflowError):
        pass

    result.set_report(report)

    return result


def parse_search_report(html: str) -> SearchResult:
    result = SearchResult()
    parser = NDBHtmlParser()

    parser.analyze(html)
    count_tag = parser.find_one('span', params={'id': 'numRec'})

    file_tag = parser.find_one('a', after=count_tag, params={'id': 'fileGal'})
    url = file_tag.attrs.get('href', '') if file_tag else ''

    file = download_file(url)
    report = parse_xls(file)

    try:
        result.set_count(int(count_tag.data))
    except (TypeError, ValueError, OverflowError, AttributeError):
        pass

    result.set_report(report)

    return result


def parse_summary(html: str) -> SummaryResult:
    report = {}
    result = SummaryResult()
    parser = NDBHtmlParser()
    parser.analyze(html)
#    print(parser.get_tree())

    summary_tag = parser.find_one('div', params={'id': 'summary'})
    if summary_tag:
        heading_tag = parser.find_one('h2', params={'class': 'justHeading'})
        if heading_tag and "NDB ID" in heading_tag.data:
            ndb_id_tag = next(heading_tag)
            if ndb_id_tag:
                report["NDB ID"] = ndb_id_tag.data
                report["PDB ID"] = ndb_id_tag.next_data()

        details_tags = parser.find_all('h3', after=heading_tag, params={'id': 'dataKey'})
        if details_tags:
            for i in range(len(details_tags) - 1):
                tag = details_tags[i]
                if 'Nucleic Acid Sequence' in tag.data:
                    chains_tags = parser.find_one('div', params={'id': 'naSeq'})
                    if chains_tags:
                        report['Nucleic Acid Sequence'] = {}
                        for chain_tag in chains_tags.children:
                            if chain_tag and chain_tag.attrs.get('class') == 'blueBoldTxt':
                                report['Nucleic Acid Sequence'][chain_tag.data] = chain_tag.next_data()
                elif 'Protein Sequence' in tag.data:
                    chains_tags = parser.find_one('div', params={'id': 'protSeq'})
                    if chains_tags:
                        report['Protein Sequence'] = {}
                        for chain_tag in chains_tags.children:
                            if chain_tag and chain_tag.attrs.get('class') == 'blueBoldTxt':
                                report['Protein Sequence'][chain_tag.data] = chain_tag.next_data()
                elif 'Primary Citation' in tag.data:
                    report['Primary Citation'] = {}
                    report['Primary Citation']['Authors'] = tag.next_data()

                    before = details_tags[i+1] if i + 1 < len(details_tags) else None
                    journal_tag = parser.find_one('i', after=tag.next(), before=before)
                    if journal_tag:
                        report['Primary Citation']['Journal'] = journal_tag.data

                    title_tag = parser.find_one('a', after=tag.next(), before=before)
                    if title_tag:
                        report['Primary Citation']['Title'] = title_tag.data
                        report['Primary Citation']['Pubmed Id'] = title_tag.attrs.get("href", "").split("/")[-1]

                        next_data = tag.next().next_data()
                        if next_data:
                            next_data = next_data.split(',')
                            try:
                                report['Primary Citation']['Year'] = next_data[-1]
                                report['Primary Citation']['pp'] = next_data[-2]
                            except IndexError:
                                pass
                    else:
                        next_data = tag.next().next_data()
                        if next_data:
                            next_data = next_data.split(',')
                            try:
                                report['Primary Citation']['Year'] = next_data[-1]
                                report['Primary Citation']['pp'] = next_data[-2]
                                report['Primary Citation']['Title'] = ','.join(next_data[:-3])
                            except IndexError:
                                pass
                elif 'Download Data' in tag.data:
                    print("Download: ", str(tag))
                elif 'Cell Constants' in tag.data:
                    text = ''
                    next_tag = next(tag)
                    while next_tag and next_tag.name == 'p':
                        text += next_tag.data
                        next_tag = next(next_tag)

                    pattern = re.compile(r"([^\W\d])\s+=\s+([\d\.]+)", re.UNICODE)
                    matches = pattern.findall(text)
                    if matches:
                        report['Cell Constants'] = {}
                        for match in matches:
                            if 'α' == match[0]:
                                report['Cell Constants']['alpha'] = match[1]
                            elif 'β' == match[0]:
                                report['Cell Constants']['beta'] = match[1]
                            elif 'γ' == match[0]:
                                report['Cell Constants']['gamma'] = match[1]
                            else:
                                report['Cell Constants'][match[0]] = match[1]
                else:
                    report[tag.data.replace(":", "")] = tag.next_data()

    result.update(report)
    return result


def download_file(url: str) -> io.BytesIO:
    if url:
        with requests.session() as session:
            resp = session.get(NDBBase.siteUrl + url)
            return io.BytesIO(resp.content)
    return None
