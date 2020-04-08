# read sentence
sentence = input()

# convert sentence to lowercase
# NOTE: guarantees case insensitive processing of sentence
sentence = sentence.lower()

# count number of different vowels in the sentence
count = 0
for vowel in 'aeiou':
    if vowel in sentence:
        count += 1

plural = 's'
different = ' different'
if count == 0:
    count = 'no'
    different = ''
elif count == 1:
    count = 'only 1'
    plural = ''

print(f'The sentence contains {count}{different} vowel{plural}.')