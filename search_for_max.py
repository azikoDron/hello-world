a = [2, 1, 2, 1, 3, 5, 2, 2, 3, 1, 0, 1, 5, 0, 4]


def two_max_indexes(tmp_list: list):
    '''

    when sequence is important!
    find max element index in list and return tuple of one index
    if two max elements in list return tuple of both indexes
    :param tmp_list: list
    :return: tuple
    '''
    first_max_index = tmp_list.index(max(tmp_list))
    second_max_index = first_max_index + tmp_list[first_max_index + 1:].index(max(tmp_list[first_max_index + 1:])) + 1
    if tmp_list[first_max_index] == tmp_list[second_max_index]:
        return first_max_index, second_max_index
    return first_max_index,


print(two_max_indexes(a))
