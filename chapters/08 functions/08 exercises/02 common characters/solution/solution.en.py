def common_characters(word1, word2):

    """
    >>> common_characters('bee', 'tween')
    1
    """

    count = 0
    common_characters = ''
    for character in word1:
        if character in word2 and character not in common_characters:
            count += 1
            common_characters += character

    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
