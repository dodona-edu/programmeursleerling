How often do words appear in a text?

### Assignment

Write a function `word_count` that takes a string $$s$$ (`str`). The function must return a dictionary (`dict`) that maps each word in $$s$$ onto the number of occurrences of the word in $$s$$. Words are defined as the longest sequence of letters (where every character that is not a letter is considered a word boundary). The function may not make a distinction between uppercase and lowercase letters, and must lowercase words as keys in the dictionary it returns.

### Example

```console?lang=python&prompt=>>>
>>> text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as he could, and chuck as much as a woodchuck would If a woodchuck could chuck wood.'
>>> words = word_count(tekst)
>>> words['wood']
>>> words['chunck']
```
