def make_check_if_number_in_range(range_start, range_end):
    def number_in_range_checker(number):
        if number < range_start or number > range_end:
            return False
        return True
    return number_in_range_checker


if __name__ == '__main__':
    checkted_number = make_check_if_number_in_range(1.5, 10)
    print checkted_number(8)
