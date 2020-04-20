Write a program `sum` that takes zero or more arguments. If at least one of the arguments is not an integer value, the program must print the message `sum: invalid arguments` to `stderr` and end with *exit status* 1. Otherwise, the program must print the sum of the integer arguments to `stdout` and end with *exit status* 0.

### Example

```console?lang=bash&prompt=$
$ python ./sum
0
$ python ./sum 1 2 3 4 5 6 7 8 9 10
55
$ python ./sum 1 -2 3 -4 5 -6 7 -8 9 -10
-5
$ python ./sum a b c
sum: invalid arguments
$ echo $?
1
```
