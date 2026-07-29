Use the `Counter` class to list
the five most common letters in a text, with their counts.

### Assignment

Write a function `most_common_letters` that takes a string (`str`) and returns a list of `(letter, count)` tuples for the five most common letters in the text. Only letters count: characters that are not letters must be ignored, and case must be ignored (uppercase and lowercase versions of the same letter are added together, and reported in lowercase). If two or more letters occur equally often, list them in the order they first appear in the text. If the text contains fewer than five distinct letters, return only those that occur.

### Example

```console?lang=python&prompt=>>>
>>> most_common_letters('mississippi')
[('i', 4), ('s', 4), ('p', 2), ('m', 1)]
>>> most_common_letters('AaAaBbBcCcC')
[('a', 4), ('c', 4), ('b', 3)]
```
