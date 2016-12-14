def biggest_area(array):
    result = 0
    for i, item in enumerate(array):
        if item == 0:
            continue
        length = 1
        height = item
        position = i
        while position < len(array) - 1:
            if array[position + 1] >= item:
                length += 1
            else:
                break
            position += 1
        position = i
        while position > 0:
            if array[position - 1] >= item:
                length += 1
            else:
                break
            position -= 1
        print length, height
        temporary_result = length * height
        if temporary_result > result:
            result = temporary_result
    return result


if __name__ == '__main__':
    print biggest_area([4, 0, 3, 4])
