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








# def hourly_time_divider(tmp_list):
#    '''
#
#    :param tmp_list: is list of str form of hours '11:25'
#    :return: list contains []*12, divided hourly in each list
#    '''
#    filtered_list = []
#    up = [[], [], [], [], [], [], [], [], [], [], [], []]
#    hours = [str(hour) for hour in range(8, 20)]  # working till 20:00
#    counter = 0
#    for lis in tmp_list:
#        li = lis.replace(':', '')
#        filtered_list.append(li)
#    for hour in hours:
#
#        for x in filtered_list:
#            if hour in x[0:2]:
#                up[counter].append(x)
#                counter += 1
#    return up
#
# print(hourly_time_divider(temporary_list))
#
#
# alk = []
# items = [820, 840, 859,900,910]
# times = [800, 900, 1000, 1100,1200]
# counter = 0
# for x in items:
#    if x in range(times[counter]-1, times[counter+1]):
#        alk.append(x)
#    else:
#        counter += 1
#
