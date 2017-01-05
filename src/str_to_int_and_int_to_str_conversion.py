def conversion_string_to_integer(string_number):
    """Converts string to integer.

    Args:
        string_number (str): String that would be converted to integer.

    Returns:
        int: Converted number.

    Raises:
        ValueError: Raised when string contains characters that are not digits.
    """
    result = 0
    for i, digit in enumerate(string_number):
        if ord(digit) < ord('0') or ord(digit) > ord('9'):
            raise ValueError
        result += (
            (ord(digit) - ord('0')) * (10 ** (len(string_number) - 1 - i))
        )
    return result


def conversion_integer_to_string(number):
    """Converts integer to string.

    Args:
        number (int): Number that would be converted to string.

    Returns:
        str: Converted string
    """
    string_of_digits = ''
    while number >= 10:
        digit = number % 10
        string_of_digits = chr(ord('0') + digit) + string_of_digits
        number = number / 10
    string_of_digits = chr(ord('0') + number) + string_of_digits
    return string_of_digits


if __name__ == '__main__':
    print conversion_string_to_integer('123')
    print conversion_integer_to_string(10763)
