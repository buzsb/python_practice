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


if __name__ == '__main__':
    print conversion_string_to_integer('123')
