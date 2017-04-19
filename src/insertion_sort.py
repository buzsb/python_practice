def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        value = unsorted_list[i]
        j = i
        while j > 0 and value < unsorted_list[j - 1]:
            unsorted_list[j] = unsorted_list[j - 1]
            j -= 1
        unsorted_list[j] = value
    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [2, 4, 1, 6, 5]
    print insertion_sort(unsorted_list)
