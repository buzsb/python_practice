import re


def first_crt_uppercase(string):
    match = re.match(r'^[A-Z]', string)
    if match:
        print "Yes sting starts with uppercase character"
    return match


def last_crt_number(string):
    match = re.match(r'.*\d', string)
    if match:
        print "Last character in string is number"
    return match


def is_there_only_love(string):
    match = re.match(r'[love]*$', string)
    if match:
        print "only love"
    return match


if __name__ == '__main__':
    first_crt_uppercase('Aloha')
    last_crt_number('sring 3')
    is_there_only_love('lllooove')
