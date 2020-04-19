A person's full name consists of two words, next to each other, consisting of only letters from the alphabet, all lower case except for the first one, which is upper case. Between
the two words there should only be white spaces. The words start and end at a word boundary. E.g., according to this specification Cardinal Richelieu is a name, but Charles d'Artagnan is not, and neither is Gilbert duPrez, Joe DiMaggio, or Unit X1138.

### Assignment

Write a function `names` that takes the location of a text file (`str`). The function must return a `list` containing all presumable names in the given text file. A presumable name is a sequence of two words that meets the above description.

### Example

In the following interactive session we assume the text file [`data.en.txt`](media/data/data.en.txt){:target="_blank"} to be located in the current directory.

```console?lang=python&prompt=>>>
>>> names('data.en.txt')
['Monty Python', 'Flying Circus', 'Graham Chapman', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Monty Python', 'Holy Grail', 'The Meaning', 'North\nAmerica', 'Saturday Night']
```
