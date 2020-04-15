"""
>>> word_split('data.txt')
['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood', 'He', 'would', 'chuck', 'he', 'would', 'as', 'much', 'as', 'he', 'could', 'And', 'chuck', 'as', 'much', 'as', 'a', 'woodchuck', 'would', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood']
>>> word_count('data.txt')
{'how': 1, 'much': 3, 'wood': 3, 'would': 4, 'a': 4, 'woodchuck': 4, 'chuck': 5, 'if': 2, 'could': 3, 'he': 3, 'as': 4, 'and': 1}
"""

def word_split(filename):

    word = ''
    words = []
    for line in open(filename, 'r'):
        for character in line:
            if character.isalpha():
                word += character
            else:
                if word:
                    words.append(word)
                word = ''

        if word:
            words.append(word)

    return words

def word_count(filename):

    words = {}
    for word in map(str.lower, word_split(filename)):
        words[word] = words.get(word, 0) + 1

    return words

if __name__ == '__main__':
    import doctest
    doctest.testmod()
