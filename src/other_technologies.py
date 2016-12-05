def cubed_list(array):
    cubed_list = list(map(lambda i: i**3, array))
    return cubed_list


if __name__ == '__main__':
    print cubed_list([2, 3, 4])
