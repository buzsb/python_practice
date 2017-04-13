import re


def password_validity_checker(passwords_list):
    good_passwords_list = []
    passwords = passwords_list.split(',')
    for password in passwords:
        if len(password) < 6 and len(password) > 12:
            continue
        elif not re.search(r'[A-Z]', password):
            continue
        elif not re.search(r'[a-z]', password):
            continue
        elif not re.search(r'[0-9]', password):
            continue
        elif not re.search(r'[$#@]', password):
            continue
        else:
            good_passwords_list.append(password.strip())
    return good_passwords_list


if __name__ == '__main__':
    passwords = 'password, 1111, P23Una#jd, GoodPass1$'
    print password_validity_checker(passwords)
