def biggest_area(array):
    result = 0
    for i in array:
        if i == 0:
            continue
        length = 1
        heigth = i
        position = array.index(i)
        while position < len(array) - 1:
            if array[position + 1] >= i:
                length += 1
            else:
                break
            position += 1

        temporary_result = length * heigth
        print temporary_result
        if temporary_result > result:
            result = temporary_result
    return result


if __name__ == '__main__':
    print biggest_area([3, 2, 3])
