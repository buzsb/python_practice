def make_check_if_number_in_range(x, y):
    def number_in_range_checker(n):
        if n in range(x, y):
            return True
    return number_in_range_checker


if __name__ == '__main__':
    checkted_number = make_check_if_number_in_range(1, 10)
    print checkted_number(8)
