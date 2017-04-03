def binary_search(sorted_list, searched_element):
    if sorted_list == []:
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
    if sorted_list == []:
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


if __name__ == '__main__':
    array = [1, 2, 3, 5]
    print binary_search(array, 5)
    print recursive_binary_search(array, 1)
