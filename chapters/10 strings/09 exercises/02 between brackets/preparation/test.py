def contains(word, sentence):

    """
    >>> contains('wonder', 'And now for something completely different')
    True
    >>> contains('wonder', 'Always look on the bright side of life.')
    False
    """

    index = -1
    for character in word:
        index = sentence.find(character, index + 1)
        if index == -1:
            return False

    return True

def hide(word, sentence):

    """
    >>> hide('wonder', 'And now for something completely different')
    'And no[w] f[o]r somethi[n]g completely [d]iff[er]ent'
    >>> hide('wonder', 'Always look on the bright side of life.')
    'Al[w]ays l[o]ok o[n] the bright si[de] of life.'
    """

    hidden = ''
    open = False
    index = 0
    word = word.lower()
    for character in sentence:
        if index < len(word) and character.lower() == word[index]:
            if not open:
                hidden += '['
            open = True
            index += 1
        elif open:
            hidden += ']'
            open = False
        hidden += character

    if open:
        hidden += ']'

    return hidden

if __name__ == '__main__':
    import doctest
    doctest.testmod()