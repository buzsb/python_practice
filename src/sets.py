def unique_elements_in_list(array):

    unique_elements = [i for i in set(array)]
    print unique_elements
    return unique_elements

list1 = [2, 3, 4, 2, 3]
list2 = [3, 4, 6, 9, 3, 4, 2]

def common_elments_in_lists(first_list, second_list):
    common_list = []
    for i in first_list:
        if i in second_list and i not in common_list:
            common_list.append(i)
    print common_list
    return common_list

def common_elments_in_lists_set(first_list, second_list):
    common_list = []
    for i in first_list:
        if i in set(second_list) and i not in common_list:
            common_list.append(i)
    print common_list
    return common_list


if __name__ == '__main__':
    unique_elements_in_list([1, 2, 3, 3, 4, 4])

    common_elments_in_lists(list1, list2)

    common_elments_in_lists_set(list1, list2)
