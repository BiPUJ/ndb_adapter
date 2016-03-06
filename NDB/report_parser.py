from NDB.html_parser import NDBHtmlParser


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

    count = parser.get_data_by_attr('span', 'id', 'numRec')
    count = 0 if not count else int(count)

    result['count'] = count
    result['report'] = ''

    return result

