from NDB.html_parser import NDBHtmlParser
import re

def parse_to_table(text):
    return [t.strip() for t in text.splitlines()]


def parse_csv(table):
    result = []
    headers = table[0].split(',')
    headers_len = len(headers) - 1

    for elem in table[1:]:
        record = {}; after = 0
        values = elem.split(',')
        values_len = len(values) - 1

        for i in range(headers_len + 1):
            if 'Authors' in headers[i]:
                after = headers_len - i
                after = values_len - after + 1
            #     print(str(i) + " " + str(after))
                record[headers[i]] = ",".join(values[i:after])
            else:
                if after > 0:
                    val = after
                    after += 1
                else:
                    val = i
                # print("val " + str(val) + ", val_len " + str(values_len) + ", after " + str(after) + ", i " + str(i))
                # print(values)
                record[headers[i]] = values[val]

        result.append(record)

    return result


def parse_advanced_search_report(text):
    result = {}

    raw_table = parse_to_table(text)
    count = raw_table[1].rpartition(': ')[-1]
    report = parse_csv(raw_table[2:])

    result['count'] = int(count) if count != raw_table[1] else 0
    result['report'] = report

    return result


def parse_search_report(html):
    result = {}
    parser = NDBHtmlParser()

    parser.analyze(html)
    #print(str(tree))
    count_tag = parser.find_one('span', params={'id': 'numRec'})
    count = 0 if not count_tag else int(count_tag.data)

    file_tag = parser.find_one('a', after=count_tag, params={'id': 'fileGal'})
    url = file_tag.attrs['href'] if file_tag and 'href' in file_tag.attrs else ''

    result['count'] = count
    result['report'] = {
        'fileUrl': url
    }

    return result


def parse_summary(html):
    result = {}
    parser = NDBHtmlParser()
    #print(html)
    parser.analyze(html)
    #print(parser.get_tree())
    summary_tag = parser.find_one('div', params={'id': 'summary'})
    #print(str(summary_tag))
    if summary_tag:
        heading_tag = parser.find_one('h2', params={'class': 'justHeading'})
        #print(str(heading_tag))
        if heading_tag and "NDB ID" in heading_tag.data:
            ndb_id_tag = next(heading_tag)
            if ndb_id_tag:
                result["NDB ID"] = ndb_id_tag.data
                result["PDB ID"] = ndb_id_tag.next_data()

        details_tags = parser.find_all('h3', after=heading_tag, params={'id': 'dataKey'})
        if details_tags:
            for i in range(len(details_tags) - 1):
                tag = details_tags[i]
                if 'Nucleic Acid Sequence' in tag.data:
                    chains_tags = parser.find_one('div', params={'id': 'naSeq'})
                    if chains_tags:
                        result['Nucleic Acid Sequence'] = {}
                        for chain_tag in chains_tags.children:
                            if chain_tag and 'class' in chain_tag.attrs and chain_tag.attrs['class'] == 'blueBoldTxt':
                                result['Nucleic Acid Sequence'][chain_tag.data] = chain_tag.next_data()
                elif 'Protein Sequence' in tag.data:
                    chains_tags = parser.find_one('div', params={'id': 'protSeq'})
                    if chains_tags:
                        result['Protein Sequence'] = {}
                        for chain_tag in chains_tags.children:
                            if chain_tag and 'class' in chain_tag.attrs and chain_tag.attrs['class'] == 'blueBoldTxt':
                                result['Protein Sequence'][chain_tag.data] = chain_tag.next_data()
                elif 'Primary Citation' in tag.data:
                    result['Primary Citation'] = {}
                    result['Primary Citation']['Authors'] = tag.next_data()

                    before = details_tags[i+1] if i + 1 < len(details_tags) else None
                    journal_tag = parser.find_one('i', after=tag.next(), before=before)
                    if journal_tag:
                        result['Primary Citation']['Journal'] = journal_tag.data

                    title_tag = parser.find_one('a', after=tag.next(), before=before)
                    if title_tag:
                        result['Primary Citation']['Title'] = title_tag.data
                        if 'href' in title_tag.attrs:
                            result['Primary Citation']['Pubmed Id'] = title_tag.attrs["href"].split("/")[-1]

                        next_data = tag.next().next_data()
                        if next_data:
                            next_data = next_data.split(',')
                            try:
                                result['Primary Citation']['Year'] = next_data[-1]
                                result['Primary Citation']['pp'] = next_data[-2]
                            except IndexError:
                                pass
                    else:
                        #print("Primary Cit: ", str(tag.next().next_data()))
                        next_data = tag.next().next_data()
                        if next_data:
                            next_data = next_data.split(',')
                            try:
                                result['Primary Citation']['Year'] = next_data[-1]
                                result['Primary Citation']['pp'] = next_data[-2]
                                result['Primary Citation']['Title'] = ','.join(next_data[:-3])
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
                        result['Cell Constants'] = {}
                        for match in matches:
                            if 'α' == match[0]:
                                result['Cell Constants']['alpha'] = match[1]
                            elif 'β' == match[0]:
                                result['Cell Constants']['beta'] = match[1]
                            elif 'γ' == match[0]:
                                result['Cell Constants']['gamma'] = match[1]
                            else:
                                result['Cell Constants'][match[0]] = match[1]
                else:
                    result[tag.data] = tag.next_data()

    return result