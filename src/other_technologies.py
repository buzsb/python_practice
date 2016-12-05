def cubed_list(array):
    cubed_list = map(lambda i: i**3, array)
    return cubed_list


def other_cubed_list(array):
    cubed_list = [i**3 for i in array]
    return cubed_list


def bigger_than_n(array, n):
    bigger_list = filter(lambda i: i > n, array)
    return bigger_list


def other_bigger_than_n(array, n):
    bigger_list = [i for i in array if i > n]
    return bigger_list


def product_list(array):
    product = reduce((lambda x, y: x * y), array)
    return product


if __name__ == '__main__':
    print cubed_list([2, 3, 4])
    print other_cubed_list([2, 3, 4])
    print bigger_than_n([2, 3, 5, 7, 8], 5)
    print other_bigger_than_n([2, 3, 5, 7, 8], 5)
    print product_list([2, 3, 4])
