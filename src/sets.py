def unique_elements_in_list(array):

    unique_elements = [i for i in set(array)]
    print unique_elements
    return unique_elements


if __name__ == '__main__':
    unique_elements_in_list([1, 2, 3, 3, 4, 4])
    