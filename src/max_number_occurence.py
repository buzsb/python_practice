import random

from collections import defaultdict


def generated_list(number):
    random_generated_list = []
    while len(random_generated_list) < number:
        random_generated_list.append(random.randint(0, 100))
    print random_generated_list
    return random_generated_list


def generated_dictionary(numbers_list):
    numbers_occurrences = defaultdict(int)

    for i in numbers_list:
        numbers_occurrences[i] += 1

    return numbers_occurrences


def max_number_occurrence(generated_list):
    if generated_list == []:
        raise ValueError

    dictionary = generated_dictionary(generated_list)

    items_list = dictionary.items()
    sorted_items_list = sorted(
        items_list, key=lambda max_item_value: max_item_value[1]
    )

    result = sorted_items_list[-1]

    print (
        'Number {number} have max occurrence in list \n'
        'namely {repeats} times'
        .format(number=result[0], repeats=result[1])
    )

    return result


if __name__ == '__main__':
    max_number_occurrence(generated_list(10))
