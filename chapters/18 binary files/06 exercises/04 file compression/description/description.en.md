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