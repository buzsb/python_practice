def add(a, b):
    """Basic function which adds two numbers"""
    return a + b 


def factorial(number):
    n = 1
    if not isinstance(number, int):
        raise ValueError("Number is not integral.")
    if number < 0:
        raise ValueError("Number is less than 0.")
    for i in range(number):
        n = n * (i + 1)
    return n


if __name__ == '__main__':
    print add(2, 3)

    print factorial(4)