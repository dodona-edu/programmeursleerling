Count how often each letter occurs in a
string (case-insensitively). You can ignore every character that is not
a letter. Print the letters with their counts, in order from highest
count to lowest count.

### Assignment

Write a function `letter_count` that takes a string (`str`). The function must print how often each letter occurs in the given string, one letter per line, formatted as the letter followed by a colon, a space and the number of times it occurs. Do not distinguish between uppercase and lowercase letters, and print the letters in lowercase. Characters that are not letters must be ignored. Print the letters from most to least frequent, and put letters that occur equally often in alphabetical order.

### Example

```console?lang=python&prompt=>>>
>>> letter_count('Hello, World!')
l: 3
o: 2
d: 1
e: 1
h: 1
r: 1
w: 1
>>> letter_count('12345 + 67890 = ?')
```
