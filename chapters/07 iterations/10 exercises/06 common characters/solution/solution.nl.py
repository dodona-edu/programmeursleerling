# twee regels inlezen
regel1 = input()
regel2 = input()

# gemeenschappelijke karakters bepalen
gemeenschappelijk = ''
for karakter in regel1:
    if karakter in regel2 and karakter not in gemeenschappelijk:
        gemeenschappelijk += karakter

# gemeenschappelijke karakters uitschrijven
print(gemeenschappelijk)
