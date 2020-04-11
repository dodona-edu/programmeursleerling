Sometimes runtime errors occur not because you made a programming
mistake, but because your program encountered a situation that you could
not foresee when you wrote it. This is particularly relevant when you
deal with files: for instance, when you access a file on a USB-stick,
and the user pulls out the USB-stick during the file processing,
obviously an error occurs that you cannot really account for in your
code. Every runtime error raises a so-called "exception," and you can
"capture" such exceptions if you want to deal with them in your program,
rather than make the program end abruptly.
