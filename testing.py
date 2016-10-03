import parsing

debug_links_knowledge = ['http://developer.rutoken.ru/display/KB/CP1001',
                         'http://developer.rutoken.ru/display/KB/CP1002',
                         'http://developer.rutoken.ru/display/KB/CP1003',
                         'http://developer.rutoken.ru/display/KB/CP1004',
                         'http://developer.rutoken.ru/display/KB/CP1005',
                         'http://developer.rutoken.ru/display/KB/CP1006',
                         'http://developer.rutoken.ru/display/KB/CP1007',
                         'http://developer.rutoken.ru/display/KB/CP1008',
                         'http://developer.rutoken.ru/display/KB/CP1009',
                         'http://developer.rutoken.ru/display/KB/DM1001',
                         'http://developer.rutoken.ru/display/KB/DM1001-eng',
                         'http://developer.rutoken.ru/display/KB/DM1002',
                         'http://developer.rutoken.ru/display/KB/DM1003',
                         'http://developer.rutoken.ru/display/KB/PU1001',
                         'http://developer.rutoken.ru/display/KB/PU1002',
                         'http://developer.rutoken.ru/display/KB/PU1003',
                         'http://developer.rutoken.ru/display/KB/PU1004',
                         'http://developer.rutoken.ru/display/KB/PU1005',
                         'http://developer.rutoken.ru/display/KB/PU1006',
                         'http://developer.rutoken.ru/display/KB/PU1007',
                         'http://developer.rutoken.ru/display/KB/PU1008',
                         'http://developer.rutoken.ru/display/KB/PU1009',
                         'http://developer.rutoken.ru/display/KB/PU1010',
                         'http://developer.rutoken.ru/display/KB/PU1011',
                         'http://developer.rutoken.ru/display/KB/PU1012',
                         'http://developer.rutoken.ru/display/KB/PU1013',
                         'http://developer.rutoken.ru/display/KB/RD1001',
                         'http://developer.rutoken.ru/display/KB/RD1002',
                         'http://developer.rutoken.ru/display/KB/RD1003',
                         'http://developer.rutoken.ru/display/KB/RD1004',
                         'http://developer.rutoken.ru/display/KB/RD1005',
                         'http://developer.rutoken.ru/display/KB/RD1006',
                         'http://developer.rutoken.ru/display/KB/RD1007',
                         'http://developer.rutoken.ru/display/KB/RD1008',
                         'http://developer.rutoken.ru/display/KB/RD1009',
                         'http://developer.rutoken.ru/display/KB/RD1010',
                         'http://developer.rutoken.ru/display/KB/RD1011',
                         'http://developer.rutoken.ru/display/KB/RD1012',
                         'http://developer.rutoken.ru/display/KB/RU1001',
                         'http://developer.rutoken.ru/display/KB/RU1002',
                         'http://developer.rutoken.ru/display/KB/RU1003',
                         'http://developer.rutoken.ru/display/KB/Troubleshooting']
debug_error_links = ['http://developer.rutoken.ru/display/KB/PU1012',  # 0x6400
                     'http://developer.rutoken.ru/display/KB/PU1013',  # 0x6a82
                     'http://developer.rutoken.ru/display/KB/RD1002',  # 10
                     'http://developer.rutoken.ru/display/KB/RD1003',  # -536870387
                     'http://developer.rutoken.ru/display/KB/RD1004',  # 1060
                     'http://developer.rutoken.ru/display/KB/RD1006',  # 1053
                     'http://developer.rutoken.ru/display/KB/RD1007',  # 5
                     'http://developer.rutoken.ru/display/KB/RD1009',  # 259
                     'http://developer.rutoken.ru/display/KB/RD1012']  # 1223

debug_link_and_tags = [['http://developer.rutoken.ru/display/KB/CP1001'],
                       ['http://developer.rutoken.ru/display/KB/CP1002'],
                       ['http://developer.rutoken.ru/display/KB/CP1003', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/CP1004', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/CP1005', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/CP1006', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/CP1007', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/CP1008', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/CP1009', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/DM1001'],
                       ['http://developer.rutoken.ru/display/KB/DM1001-eng'],
                       ['http://developer.rutoken.ru/display/KB/DM1002'],
                       ['http://developer.rutoken.ru/display/KB/DM1003'],
                       ['http://developer.rutoken.ru/display/KB/PU1001', 'форматирование'],
                       ['http://developer.rutoken.ru/display/KB/PU1002'],
                       ['http://developer.rutoken.ru/display/KB/PU1003', 'kb-troubleshooting-article', 'егаис'],
                       ['http://developer.rutoken.ru/display/KB/PU1004'],
                       ['http://developer.rutoken.ru/display/KB/PU1005', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/PU1006', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/PU1007', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/PU1008', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/PU1009', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/PU1010', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/PU1011', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/PU1012', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/PU1013', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RD1001', 'логи'],
                       ['http://developer.rutoken.ru/display/KB/RD1002', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RD1003', 'kb-troubleshooting-article', '536870387',
                        'winscard'],
                       ['http://developer.rutoken.ru/display/KB/RD1004'],
                       ['http://developer.rutoken.ru/display/KB/RD1005', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RD1006', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RD1007', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RD1008', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RD1009', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RD1010', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RD1011', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RD1012', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RU1001', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RU1002', 'kb-troubleshooting-article'],
                       ['http://developer.rutoken.ru/display/KB/RU1003', 'kb-troubleshooting-article']]


def main():
    #test_tags1()
    #test_tags2()
    test_equals_tag()

def test_tags1():
    # [15]:  ['http://developer.rutoken.ru/display/KB/PU1003', 'kb-troubleshooting-article', 'егаис']
    # пришло 3 тега, совпало из них 2 -> priority2 содержит списки из ссылки и совпадающих тегов
    parsing.sort_tags(['kb-troubleshooting-article', 'егаис', 'tag3'], debug_link_and_tags[15])
    parsing.sort_tags(['kb-troubleshooting-article', 'егаис', 'tag3'], debug_link_and_tags[15])
    print('priority2: ' + str(parsing.priority2))

    parsing.priority2 = []
    for debug in debug_link_and_tags:
        parsing.sort_tags(['kb-troubleshooting-article', 'егаис', 'tag3'], debug)
    list_of_len = []
    for unit in parsing.priority2:
        list_of_len.append(len(unit) - 1)
    print('priority2: ' + str(parsing.priority2))
    print(list_of_len)



def test_equals_tag():
    list1 = []
    input = ['kb-troubleshooting-article', 'егаис']
    print(parsing.equals_tags(['kb-troubleshooting-article', 'егаис','A','C'], debug_link_and_tags[15]))
    print(parsing.equals_tags(input, debug_link_and_tags[1]))

    for debug in debug_link_and_tags:
        list1.append(parsing.equals_tags(input, debug))
    for unit in list1:
        print(unit)
    list1.sort(key=sort_col, reverse=True)
    print('sort')
    for unit in list1:
        print(unit)
    for unit in list1:
        index = unit[1]
    parsing.for_sort(list1)

def sort_col(i):
    return i[1:][0]
if __name__ == "__main__":
    main()
