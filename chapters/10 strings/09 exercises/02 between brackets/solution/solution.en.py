# read text
text = input()

# collect letters enclosed between square brackets
letters = ''
enclosed = False
for character in text:
    if character == '[':
        enclosed = True
    elif character == ']':
        enclosed = False
    elif enclosed:
        letters += character

# print letters
print(letters)
