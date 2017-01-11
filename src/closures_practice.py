def make_check_if_number_in_range(range_start, range_end):
    """Check if number in some range.

    Args:
        range_start (int or float): Beginning of range.
        range_end (int of float): End of range.

    Returns:
        boolean: True or False
    """
    def number_in_range_checker(number):
        return range_start < number < range_end
    return number_in_range_checker


if __name__ == '__main__':
    checkted_number = make_check_if_number_in_range(1.5, 10)
    print checkted_number(18)
