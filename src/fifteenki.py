import random


def generated_list(number):
    array = range(number)
    random.shuffle(array)
    return array


def fifteenki(generated_list):
    if 0 in generated_list:
        generated_list[generated_list.index(0)] = ''
    print(
        '''
        {lst[0]:<3}{lst[1]:<3}{lst[2]:<3}{lst[3]:<3}
        {lst[4]:<3}{lst[5]:<3}{lst[6]:<3}{lst[7]:<3}
        {lst[8]:<3}{lst[9]:<3}{lst[10]:<3}{lst[11]:<3}
        {lst[12]:<3}{lst[13]:<3}{lst[14]:<3}{lst[15]:<3}'''
    ).format(lst=generated_list)


if __name__ == '__main__':
    fifteenki(generated_list(16))
