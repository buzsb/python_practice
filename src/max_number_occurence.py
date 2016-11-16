import random


def generated_list():
    random_generated_list = []
    while len(random_generated_list) < 10:
        random_generated_list.append(random.randint(0, 9))
    print random_generated_list
    return random_generated_list


def max_number_occurence(generated_list):
    numbers_occurensces = {}

    for i in generated_list:
        if i in  numbers_occurensces:
            numbers_occurensces[i] += 1
        else:
            numbers_occurensces[i] = 1
    return numbers_occurensces


if __name__ == '__main__':
    print max_number_occurence(generated_list())