# rotatie inlezen
rot = int(input())

# alfabet uitschrijven
alfabet = ''
for index in range(26):
    alfabet += chr(ord('A') + index)
print(alfabet)

# geroteerd alfabet uitschrijven
alfabet = ''
for index in range(26):
    index = (index + rot) % 26
    alfabet += chr(ord('A') + index)
print(alfabet)
