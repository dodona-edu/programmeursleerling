Write a function `vowel_removal` that takes the location of two text files (`str`). The function must copy the first text file to the second text file, with all vowels removed. The function must return a `tuple` with two elements: *i*) the total number of characters read from the first text file and *ii*) the total number of characters written to the second text file.

### Example

In onderstaande interactieve sessie gaan we ervan uit dat het tekstbestand [`data.txt`](media/data/data.txt){:target="_blank"} zich in de huidige directory bevindt.

```console?lang=python&prompt=>>>
>>> print(open('data.txt', 'r').read(), end='')
How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood.
>>> zonder_klinkers('data.txt', 'kopie.txt')
(190, 135)
>>> print(open('kopie.txt', 'r').read(), end='')
Hw mch wd wld  wdchck chck
f  wdchck cld chck wd?
H wld chck, h wld, s mch s h cld,
nd chck s mch s  wdchck wld
f  wdchck cld chck wd.
```
