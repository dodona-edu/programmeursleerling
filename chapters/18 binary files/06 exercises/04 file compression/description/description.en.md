This chapter is about binary
files, and the previous two exercises were not, at least, not directly.
There simply is not much that you can exercise with where binary files
are concerned; the main problems are with handling byte values, which is
what the previous two exercises were concerned with. But to round off
what these two exercises did, let's now use what you developed in them
to compress files.

Write a program that asks for an input file, that must exist, and an
output file, that should not exist. Then it asks whether you want to
compress or decompress. If you choose compress, the input file is
compressed using the method developed above, and written as the output
file. If you choose decompress, the input file is decompressed under the
assumption that it was compressed with the method developed above, and
written as the output file. So you should be able to get the original
file again by first compressing and then decompressing.

You best read the whole file in memory before (de)compressing, so that
you do not get into problems when a byte string ends in half a byte
instead of a full byte after compression. You also best treat both the
input file and the output file as binary files.

### Assignment

Instead of a program that asks for its input, write two functions that both take the location of an input file (`str`) and the location of an output file (`str`).

- Write a function `compress_file` that reads the given input file in binary mode, compresses its content with the method developed in the exercise *Compression*, and writes the result to the given output file.

- Write a function `decompress_file` that reads the given input file in binary mode, decompresses its content with the method developed in the exercise *Decompression*, and writes the result to the given output file.

Both functions read the entire input file into memory before (de)compressing it, so that it does not matter that a compressed byte string may end in half a byte. Both functions treat every byte of the input file as the character with that ordinal value, so that any file can be compressed, not just text files. Both functions must return a `tuple` with two elements: *i*) the number of bytes read from the input file and *ii*) the number of bytes written to the output file.

Both functions must also check that the input file exists and that the output file does not exist yet. If the input file does not exist, an `AssertionError` must be raised with the message `input file does not exist`. If the output file already exists, an `AssertionError` must be raised with the message `output file already exists`.

Compressing a file and decompressing the result must give back the original file.

### Example

In the interactive session below we assume the text file [`data.txt`](media/data/data.txt){:target="_blank"} is located in the current directory, and that the files `data.cmp` and `data.new` do not exist yet.

```console?lang=python&prompt=>>>
>>> compress_file('data.txt', 'data.cmp')
(13, 11)
>>> open('data.cmp', 'rb').read()
b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'
>>> decompress_file('data.cmp', 'data.new')
(11, 13)
>>> open('data.new', 'rb').read() == open('data.txt', 'rb').read()
True
>>> compress_file('data.xxx', 'data.yyy')
Traceback (most recent call last):
AssertionError: input file does not exist
>>> compress_file('data.txt', 'data.cmp')
Traceback (most recent call last):
AssertionError: output file already exists
```
