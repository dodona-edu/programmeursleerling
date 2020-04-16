Create a simple file encryption
program. Open a file and read it in binary mode. For each byte, if it is
smaller than 128, add 128; if it is bigger than or equal to 128,
subtract 128. Overwrite the byte with new value. Test the program on a
copy of a text file (make sure it is a copy, because you will destroy
the file). Check the contents of the encrypted file: they should be a
mess. However, when you run the program again, the original file should
be restored. If it isn't, you have a bug in your program. Aren't you
glad you were only working on a copy?
