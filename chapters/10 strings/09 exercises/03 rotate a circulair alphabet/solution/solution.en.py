# read rotation
rot = int(input())

# print alphabet
alphabet = ''
for index in range(26):
    alphabet += chr(ord('A') + index)
print(alphabet)

# print rotated alphabet
alphabet = ''
for index in range(26):
    index = (index + rot) % 26
    alphabet += chr(ord('A') + index)
print(alphabet)
