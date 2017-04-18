def insertion_sort(unsortet_list):
    for i in range(1, len(unsortet_list)):
        value = unsortet_list[i]
        j = i
        while j > 0 and value < unsortet_list[j - 1]:
            unsortet_list[j] = unsortet_list[j - 1]
            j -= 1
        unsortet_list[j] = value
    return unsortet_list


if __name__ == '__main__':
    unsortet_list = [2, 4, 1, 6, 5]
    print insertion_sort(unsortet_list)
