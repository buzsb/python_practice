def integer_conversion(string_number):
    result = 0
    for i, digit in enumerate(string_number):
        if ord(digit) < 48 or ord(digit) > 58:
            raise ValueError
        result += (ord(digit) - 48) * 10 ** (len(string_number) - 1 - i)
    return result


if __name__ == '__main__':
    print integer_conversion('123')
