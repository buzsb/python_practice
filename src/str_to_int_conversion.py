def conversion_string_to_integer(string_number):
    result = 0
    for i, digit in enumerate(string_number):
        if ord(digit) < ord('0') or ord(digit) > ord('9'):
            raise ValueError
        result += (
            (ord(digit) - ord('0')) * (10 ** (len(string_number) - 1 - i))
        )
    return result


if __name__ == '__main__':
    print conversion_string_to_integer('123')
