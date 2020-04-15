What words do three text files have in common?

### Assignment

A word in a text is defined as the longest sequence of letters, where every character that is not a letter is considered a word boundary.

Write a function `common_words` that takes the locations of three text files (`str`). The function must return a `set` containing the words that occur in all three text files. The function must return a `set` containing the words that occur in all three text files. The function may not make a distinction between uppercase and lowercase letters, and the words in the `set` must be lowercase.

### Example

In the following interactive session we assume the text files [`data_a.txt`](media/data/data_a.txt){:target="_blank"}, [`data_b.txt`](media/data/data_b.txt){:target="_blank"} and [`data_c.txt`](media/data/data_c.txt){:target="_blank"} to be located in the current directory.

```console?lang=python&prompt=>>>
>>> common_words('data_a.txt', 'data_b.txt', 'data_c.txt')
{'and', 'as', 'he'}
```
