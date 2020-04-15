How often do words appear in a text?

### Assignment

A word in a text is defined as the longest sequence of letters, where every character that is not a letter is considered a word boundary. Your task:

- Write a function `word_split` that takes the location of a text file (`str`). The function must return a `list` containing the sequence of words from the given text file.

- Write a function `word_count` that takes the location of a text file (`str`). The function must return a dictionary (`dict`) that maps each word in the given text file onto the number of occurrences of the word in the given text file. The function may not make a distinction between uppercase and lowercase letters, and must lowercase words as keys in the dictionary it returns.

{:class="callout callout-info"}
> #### Note
> This is the exact same assignment as the previous assignment, but now you have
> to make sure to process the text line by line. This is something that you 
> would have to do if you had to process a very long text.

### Example

In the following interactive session we assume the text file [`data.txt`](media/data/data.txt){:target="_blank"} to be located in the current directory.

```console?lang=python&prompt=>>>
>>> worden_split('data.txt')
['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood', 'He', 'would', 'chuck', 'he', 'would', 'as', 'much', 'as', 'he', 'could', 'And', 'chuck', 'as', 'much', 'as', 'a', 'woodchuck', 'would', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood']
>>> word_count('data.txt')
{'how': 1, 'much': 3, 'wood': 3, 'would': 4, 'a': 4, 'woodchuck': 4, 'chuck': 5, 'if': 2, 'could': 3, 'he': 3, 'as': 4, 'and': 1}
```
