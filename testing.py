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
    test_tags1()
    #test_tags2()

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
        list_of_len.append(len(unit))
    print('priority2: ' + str(parsing.priority2))
    print(list_of_len)


def test_tags2():
    # Priority1 содержит список ссылок из которых все полностью соответствуют заданным тегам,
    # сами теги не входят в Priority1 нужно добавить их отдельно (для вывода)
    input = ['kb-troubleshooting-article']
    for debug in debug_link_and_tags:
        parsing.sort_tags(input, debug)
    parsing.priority1.append(input) #
    print('priority1: ' + str(parsing.priority1))


    for debug in debug_link_and_tags:
        parsing.sort_tags(['логи'], debug)
    print('priority1: ' + str(parsing.priority1))


    parsing.priority1 = []
    input = ['kb-troubleshooting-article', '536870387', 'winscard']
    for debug in debug_link_and_tags:
        parsing.sort_tags(input, debug)
    parsing.priority1.append(input)
    print('priority1: ' + str(parsing.priority1))

if __name__ == "__main__":
    main()
