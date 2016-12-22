def repeated_words(words_array):
    repeated = set()
    result = set()
    for word in words_array:
        word = word.lower()
        if word in repeated:
            result.add(word)
        else:
            repeated.add(word)
    return result


if __name__ == '__main__':
    print repeated_words(['cat', 'Cat', 'doG', 'dog', 'COW'])
