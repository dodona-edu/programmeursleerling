# read sentence
sentence = input()

# Check if a sentence was given
if len(sentence) <= 0:
    exit()

# Capitalize first letter
newsentence = sentence[0].upper() + sentence[1:]

wordlist = newsentence.split()
lastword = ""
newsentence = ""

for word in wordlist:

    # Correct double capitals
    if len(word) > 2 and word[0] >= "A" and word[0] <= "Z" and \
            word[1] >= "A" and word[1] <= "Z" and word[2] >= "a" and \
            word[2] <= "z":
        word = word[0] + word[1].lower() + word[2:]

    # Capitalize days
    day = word.lower()
    if day == "sunday" or day == "monday" or day == "tuesday" or \
            day == "wednesday" or day == "thursday" or \
            day == "friday" or day == "saturday":
        word = day[0].upper() + day[1:]

    # Correct CAPS LOCK
    if word[0] >= "a" and word[0] <= "z":
        allcaps = True
        for c in word[1:]:
            if not (c >= "A" and c <= "Z"):
                allcaps = False
                break
        if allcaps:
            word = word[0].upper() + word[1:].lower()

    # Remove duplicates
    if word == lastword:
        continue

    newsentence += word + " "
    lastword = word

newsentence = newsentence.strip()
print(newsentence)
