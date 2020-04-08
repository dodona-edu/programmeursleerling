# read two lines
line1 = input()
line2 = input()

# determine common characters
common = ''
for character in line1:
    if character in line2 and character not in common:
        common += character

# print common characters
print(common)
