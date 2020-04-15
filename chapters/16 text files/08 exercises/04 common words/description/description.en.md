What words do three text files have in common?

### Assignment

A word in a text is defined as the longest sequence of letters, where every character that is not a letter is considered a word boundary.

Write a function `common_words` that takes the locations of three text files (`str`). The function must return a `set` containing the words that occur in all three text files. The function must return a `set` containing the words that occur in all three text files. The function may not make a distinction between uppercase and lowercase letters, and the words in the `set` must be lowercase.

### Example

In the following interactive session we assume the text files [`data_a.txt`](media/data/data_a.txt){:target="_blank"}, [`data_b.txt`](media/data/data_b.txt){:target="_blank"} and [`data_c.txt`](media/data/data_c.txt){:target="_blank"} to be located in the current directory.

```console?lang=python&prompt=>>>
>>> worden_split('data.txt')
['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood', 'He', 'would', 'chuck', 'he', 'would', 'as', 'much', 'as', 'he', 'could', 'And', 'chuck', 'as', 'much', 'as', 'a', 'woodchuck', 'would', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood']
>>> word_count('data.txt')
{'how': 1, 'much': 3, 'wood': 3, 'would': 4, 'a': 4, 'woodchuck': 4, 'chuck': 5, 'if': 2, 'could': 3, 'he': 3, 'as': 4, 'and': 1}
```
