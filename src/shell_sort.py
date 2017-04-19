def shell_sort(unsorted_list):
    gap = len(unsorted_list) / 2
    while gap > 0:
        for i in range(gap, len(unsorted_list)):
            value = unsorted_list[i]
            j = i
            while j >= gap and value < unsorted_list[j - gap]:
                unsorted_list[j] = unsorted_list[j - gap]
                j -= gap
            unsorted_list[j] = value
        gap /= 2
    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [2, 4, 1, 6, 5]
    print shell_sort(unsorted_list)
