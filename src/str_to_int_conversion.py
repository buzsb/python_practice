def integer_conversion(string_number):
    numbers_list = []
    for i in string_number:
        if ord(i) >= 48 and ord(i) <= 58:
            numbers_list.append(ord(i) - 48)
    result = 0
    for i, number in enumerate(numbers_list):
        result += number * 10 ** (len(numbers_list) - 1 - i)
    return result


if __name__ == '__main__':
    print integer_conversion('12l3')
