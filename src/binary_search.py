def binary_search(sorted_list, searched_element):
    start = 0
    end = len(sorted_list)
    while start <= end:
        middle_element = (start + end) / 2
        if sorted_list[middle_element] == searched_element:
            return middle_element

        if sorted_list[middle_element] < searched_element:
            start = middle_element + 1
        else:
            end = middle_element - 1
    return None


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 7]
    print binary_search(array, 6)
