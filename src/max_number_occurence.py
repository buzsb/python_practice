import random


def generated_list():
    random_generated_list = []
    while len(random_generated_list) < 10:
        random_generated_list.append(random.randint(0, 9))
    return random_generated_list


def max_number_occurence():
    numders_occurensces = {}

    for i in generated_list():
        if numders_occurensces.has_key(i):
            numders_occurensces[i] += 1
        else:
            numders_occurensces[i] = 1
    return numders_occurensces


if __name__ == '__main__':
    print max_number_occurence()