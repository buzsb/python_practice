def biggest_area(array):
    result = 0
    for i in range(len(array)):
        if array[i] == 0:
            continue
        length = 1
        heigth = array[i]
        position = i
        while position < len(array) - 1:
            print position
            if array[position + 1] >= array[i]:
                length += 1
            else:
                break
            position += 1

        temporary_result = length * heigth
        if temporary_result > result:
            result = temporary_result
    return result


if __name__ == '__main__':
    print biggest_area([3, 2, 3])
