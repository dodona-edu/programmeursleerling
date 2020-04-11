def clean(s):
    news = ""
    s = s.lower()
    for c in s:
        if 'a' <= c <= 'z':
            news += c
        else:
            news += " "
    return news


# read word
word = input()

# read text
text = input()

# count number of occurrences of word in sentence
count = 0
for word2 in clean(text).split():
    if word2 == word:
        count += 1

# print number of occurrences of word in sentence
print(f'Number of times "{word}" occurs in the text: {count}')
