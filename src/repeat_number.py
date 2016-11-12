array = [1, 2, 3, 4, 2, 3, 3, 3]

def repeat_number(array):
    r_counts = 0 
    number = 0
    for i in array:
        counter = 0
        for j in array:
            if i == j:
                counter += 1 
            if counter > r_counts:
                r_counts = counter
                number = i 
    return number

if __name__ == '__main__':
    print repeat_number(array)