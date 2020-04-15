"""
>>> common_words('data_a.txt', 'data_b.txt', 'data_c.txt')
{'and', 'as', 'he'}
"""

def word_split(filename):

    word = ''
    words = set()
    for line in open(filename, 'r'):
        for character in line:
            if character.isalpha():
                word += character
            else:
                if word:
                    words.add(word.lower())
                word = ''

        if word:
            words.add(word.lower())

    return words

def common_words(filename1, filename2, filename3):

    words = word_split(filename1)
    words &= word_split(filename2)
    words &= word_split(filename3)

    return words

if __name__ == '__main__':
    import doctest
    doctest.testmod()
