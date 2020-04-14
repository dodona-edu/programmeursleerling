"""
>>> text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as he could, and chuck as much as a woodchuck would If a woodchuck could chuck wood.'
>>> word_split(text)
['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'if', 'a', 'woodchuck', 'could', 'chuck', 'wood', 'He', 'would', 'chuck', 'he', 'would', 'as', 'much', 'as', 'he', 'could', 'and', 'chuck', 'as', 'much', 'as', 'a', 'woodchuck', 'would', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood']
>>> words = word_count(text)
>>> words['wood']
3
>>> words['chuck']
5
"""

def word_split(text):

    word = ''
    words = []
    for character in text:
        if character.isalpha():
            word += character
        else:
            if word:
                words.append(word)
            word = ''

    if word:
        words.append(word)

    return words

def word_count(text):

    words = {}
    for word in map(str.lower, word_split(text)):
        words[word] = words.get(word, 0) + 1

    return words

if __name__ == '__main__':
    import doctest
    doctest.testmod()
