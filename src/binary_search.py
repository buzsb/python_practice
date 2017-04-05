def binary_search(sorted_list, searched_element):
    if not sorted_list:
        return None
    start = 0
    end = len(sorted_list) - 1
    while start <= end:
        middle_element = (start + end) / 2
        if sorted_list[middle_element] == searched_element:
            return middle_element

        if sorted_list[middle_element] < searched_element:
            start = middle_element + 1
        else:
            end = middle_element - 1
    return None


def recursive_binary_search(sorted_list, searched_element, start=0, end=None):
    if not sorted_list:
        return None
    if end is None:
        end = len(sorted_list) - 1
    if start > end:
        return None
    middle_element = (start + end) / 2
    if sorted_list[middle_element] == searched_element:
        return middle_element

    if sorted_list[middle_element] < searched_element:
        return recursive_binary_search(
            sorted_list, searched_element, middle_element + 1, end
        )
    else:
        return recursive_binary_search(
            sorted_list, searched_element, start, middle_element - 1
        )


def another_recursive_binary_search(sorted_list, searched_element):
    if not sorted_list:
        return None
    if len(sorted_list) == 1 and sorted_list[0] is not searched_element:
        return None
    start = 0
    end = len(sorted_list)
    middle_element = (start + end) / 2
    if sorted_list[middle_element] == searched_element:
        return middle_element

    if sorted_list[middle_element] < searched_element:
        position_in_right_part = another_recursive_binary_search(
            sorted_list[middle_element:], searched_element
        )
        if position_in_right_part is None:
            return None
        return position_in_right_part + middle_element
    else:
        return another_recursive_binary_search(
            sorted_list[:middle_element], searched_element
        )


if __name__ == '__main__':
    array = [1, 2, 3, 5]
    print binary_search(array, 5)
    print recursive_binary_search(array, 1)
    print another_recursive_binary_search(array, 5)
