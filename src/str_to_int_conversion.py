def number_list(string_number):
    number_list = []
    for i in string_number:
        number_list.append(ord(i) - 48)
    return number_list


def integer_conversion(string_number):
    numbers = number_list(string_number)
    result = 0
    for i, number in enumerate(numbers):
        result += number * 10 ** (len(numbers) - 1 - i)
    print result
    return result


if __name__ == '__main__':
    integer_conversion('123')
