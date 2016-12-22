def repeated_words(words_array):
    lower_case_words_array = [i.lower() for i in words_array]
    result = set()
    for i in lower_case_words_array:
        if lower_case_words_array.count(i) > 1:
            result.add(i)
    print result
    return result


if __name__ == '__main__':
    repeated_words(['cat', 'Cat', 'doG', 'dog', 'COW'])
