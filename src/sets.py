from max_number_occurence import generated_list
from decorators import run_time_decorator


def unique_elements_in_list(array):

    unique_elements = [i for i in set(array)]
    return unique_elements


list1 = generated_list(10000)
list2 = generated_list(10000)


def common_elments_in_lists(first_list, second_list):
    common_list = []
    for i in first_list:
        if i in second_list and i not in common_list:
            common_list.append(i)
    return common_list


def common_elments_in_lists_set(first_list, second_list):
    common_list = set()
    set_list = set(second_list)
    for i in first_list:
        if i in set_list and i not in common_list:
            common_list.add(i)
    return common_list


@run_time_decorator(30)
def run_common_elements_in_list(list1, list2):
    common_elments_in_lists(list1, list2)


@run_time_decorator(30)
def run_common_elements_in_list_set(list1, list2):
    common_elments_in_lists_set(list1, list2)


if __name__ == '__main__':
    print unique_elements_in_list([1, 2, 3, 3, 4, 4])

    common_elments_in_lists(list1, list2)

    common_elments_in_lists_set(list1, list2)

    run_common_elements_in_list(list1, list2)

    run_common_elements_in_list_set(list1, list2)
