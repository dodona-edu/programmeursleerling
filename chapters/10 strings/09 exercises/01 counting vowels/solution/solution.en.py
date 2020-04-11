# read text
text = input().upper()

# print number of occurrences of each vowel in the text
for vowel in 'AEIOU':
    print(f'{vowel}: {text.count(vowel)}')
