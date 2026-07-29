Do the previous exercise,
but now make sure that all anagrams are unique, even if the word
contains repetitions of letters. For example, if the word is `"bee"`,
you produce `"bee"`, `"ebe"`, and `"eeb"`.

### Assignment

Write a **generator function** `unique_anagrams` that takes a word `word` (`str`). The function must yield every distinct anagram of `word` exactly once, as a string (`str`). The order in which the anagrams are yielded does not matter.

### Example

```console?lang=python&prompt=>>>
>>> sorted(unique_anagrams("bee"))
['bee', 'ebe', 'eeb']

>>> sorted(unique_anagrams("cat"))
['act', 'atc', 'cat', 'cta', 'tac', 'tca']
```
