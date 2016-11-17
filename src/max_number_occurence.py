import random


def generated_list():
    random_generated_list = []
    while len(random_generated_list) < 10:
        random_generated_list.append(random.randint(0, 9))
    print random_generated_list
    return random_generated_list


def generated_dictionary(random_list):
    numbers_occurrensces = {}
    random_generated_list = random_list

    for i in random_generated_list:
        if i in  numbers_occurrensces:
            numbers_occurrensces[i] += 1
        else:
            numbers_occurrensces[i] = 1
    return numbers_occurrensces


def max_number_occurrence(generated_list):
    dictionary = generated_dictionary(generated_list)

    items_list = dictionary.items()
    sorted_items_list = sorted(items_list, key=lambda max_item_value: max_item_value[1])

    result = sorted_items_list[-1]

    print (
        'Number {number} have max occurrence in list \n'
        'namely {repeats} times'
        .format(number = result[0], repeats = result[1])
    )

    return result


if __name__ == '__main__':
    max_number_occurrence(generated_list())