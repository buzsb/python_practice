def repeated_words(words_array):
    repeated = set()
    result = set()
    for i in words_array:
        i = i.lower()
        if i in repeated:
            result.add(i)
        else:
            repeated.add(i)
    return result


if __name__ == '__main__':
    print repeated_words(['cat', 'Cat', 'doG', 'dog', 'COW'])
