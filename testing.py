import parsing
import loggerdel
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
debug_error_links = ['http://developer.rutoken.ru/display/KB/PU1012',   # 0x6400
                     'http://developer.rutoken.ru/display/KB/PU1013',   # 0x6a82
                     'http://developer.rutoken.ru/display/KB/RD1002',   # 10
                     'http://developer.rutoken.ru/display/KB/RD1003',   # -536870387
                     'http://developer.rutoken.ru/display/KB/RD1004',   # 1060
                     'http://developer.rutoken.ru/display/KB/RD1006',   # 1053
                     'http://developer.rutoken.ru/display/KB/RD1007',   # 5
                     'http://developer.rutoken.ru/display/KB/RD1009',   # 259
                     'http://developer.rutoken.ru/display/KB/RD1012']   # 1223


def main():
    for entity in parsing.search_in_page('6'):
        loggerdel.debug(entity)


if __name__ == "__main__":
    main()
