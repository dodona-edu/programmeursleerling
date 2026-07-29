Create a simple file encryption
program. Open a file and read it in binary mode. For each byte, if it is
smaller than 128, add 128; if it is bigger than or equal to 128,
subtract 128. Overwrite the byte with new value. Test the program on a
copy of a text file (make sure it is a copy, because you will destroy
the file). Check the contents of the encrypted file: they should be a
mess. However, when you run the program again, the original file should
be restored. If it isn't, you have a bug in your program. Aren't you
glad you were only working on a copy?


### Assignment

Write a function `encrypt` that takes the location of a file (`str`). The function must read the given file in binary mode, and overwrite every byte of the file with its encrypted value: 128 is added to every byte smaller than 128, and 128 is subtracted from every byte greater than or equal to 128. The function returns nothing.

Because the encryption is its own inverse, a second call on the same file restores the original content of that file.

### Example

In the interactive session below we assume the text file [`data.txt`](media/data/data.txt){:target="_blank"} is located in the current directory.

```console?lang=python&prompt=>>>
>>> print(open('data.txt', 'r').read(), end='')
Hello, world!
>>> encrypt('data.txt')
>>> open('data.txt', 'rb').read()
b'\xc8\xe5\xec\xec\xef\xac\xa0\xf7\xef\xf2\xec\xe4\xa1\x8a'
>>> encrypt('data.txt')
>>> print(open('data.txt', 'r').read(), end='')
Hello, world!
```
