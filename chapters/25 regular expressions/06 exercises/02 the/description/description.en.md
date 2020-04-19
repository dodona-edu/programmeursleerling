Find all occurrences of the word "the" in a given text.

### Assignment

Write a function `find_the_the` that takes the location of a text file (`str`). The function must return a `list` containing all occurrences of "the" as a separate word in the given text file. No distinction must be made between uppercase and lowercase letters. Make sure that you do not include the combination "the" when it occurs as part of
another word (e.g., "thesaurus" or "ether").

### Example

In the following interactive session we assume the text file [`data.en.txt`](media/data/data.en.txt){:target="_blank"} to be located in the current directory.

```console?lang=python&prompt=>>>
>>> word_split('data.en.txt')
['Broadcast', 'by', 'the', 'BBC', 'between', 'and', 'Monty', 'Python', 's', 'Flying', 'Circus', 'was', 'conceived', 'written', 'and', 'performed', 'by', 'its', 'members', 'Graham', 'Chapman', 'John', 'Cleese', 'Terry', 'Gilliam', 'Eric', 'Idle', 'Terry', 'Jones', 'and', 'Michael', 'Palin']
```
