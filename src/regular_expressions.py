import re


def first_crt_uppercase(string):
    match = re.match(r'[A-Z]', string)
    if not match:
        return False
    return match


def last_crt_number(string):
    match = re.match(r'.*\d', string)
    if not match:
        return False
    return match


def is_there_only_love(string):
    match = re.match(r'[love]*$', string)
    if not match:
        return False
    return match


if __name__ == '__main__':
    print first_crt_uppercase('Aloha')
    print last_crt_number('sring 3')
    print is_there_only_love('lllooove')
