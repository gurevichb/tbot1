def equals_tags(list_of_input_tags, link_with_tags):
    '''
    Формируется список
    [[link,link_tag1,link_tag2,...],количество совпадений с веденными тегами, количество расхождений]
    '''
    list_list_link_eq_div = []
    equals_number = 0
    for input_tag in list_of_input_tags:
        for out_tag in link_with_tags[1:]:
            if out_tag == input_tag:
                equals_number += 1
    if equals_number >= 1:
        list_list_link_eq_div.append(link_with_tags)
        list_list_link_eq_div.append(equals_number)
        list_list_link_eq_div.append(len(link_with_tags[1:]) - equals_number)
        return list_list_link_eq_div


def list_link_eq_div(input_tag, link_and_tags):
    """
    формирует список из результатов equals_tags
    """
    list = []
    for unit in link_and_tags:
        list.append(equals_tags(input_tag, unit))
    return list


def sort_tags(full_list):
    """
    Сортирует список сначало по количеству совпадений тегов (по позрастанию).
    Генерируются подсписки по количеству совпадений,
    внутри них сортировка по количеству расхождений (по убыванию)
    """
    full_list = list(filter(None, full_list))
    full_list.sort(key=sort_col, reverse=True)
    new_list = []
    temp_list = []
    index = full_list[0][1]
    for row in full_list:
        if index == row[1]:
            temp_list.append(row)
        else:
            index = row[1]
            temp_list.sort(key=sort_col2)
            new_list.append(temp_list)
            temp_list = []
    temp_list.sort(key=sort_col2)
    new_list.append(temp_list)
    return new_list


def sort_col2(i):
    return i[2]


def sort_col(i):
    return i[1:][0]


def get_len(len, list):
    result_list = []
    index = 0
    for unit in list:
        for punit in unit:
            if index < len:
                index += 1
                result_list.append(punit[0])
    return result_list


def get(input_tags, links_and_tags):
    return get_len(6, sort_tags(list_link_eq_div(input_tags, links_and_tags)))


def main():
    pass


if __name__ == '__main__':
    main()
