def letter_count(text):

    """
    >>> letter_count('Hello, World!')
    l: 3
    o: 2
    d: 1
    e: 1
    h: 1
    r: 1
    w: 1
    """

    # count how often each letter occurs, ignoring case and non-letters
    letters = []
    counts = []
    for character in text.lower():
        if character.isalpha():
            if character in letters:
                counts[letters.index(character)] += 1
            else:
                letters.append(character)
                counts.append(1)

    # sort the letters by decreasing count, and alphabetically for equal counts
    pairs = sorted(zip(letters, counts), key=lambda pair: (-pair[1], pair[0]))

    # print each letter together with its count
    for letter, count in pairs:
        print(f'{letter}: {count}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
