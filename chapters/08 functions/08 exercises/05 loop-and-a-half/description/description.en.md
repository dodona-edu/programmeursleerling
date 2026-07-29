In Chapter
8,
the loop-and-a-half was explained. The final code for the example that
was presented is given below, and I made the remark that there is still
something ugly about this code, namely the fact that if `x` is smaller
than zero or higher than 1000, the code still asks for `y` even when it
can know that it has to ask a new value for `x`. I also remarked that
you can resolve this in an easy way by using a function. Create a
function and insert it in this code, so that this issue gets fixed. Also
get rid of the `exit()` and thus the possible ugly output by introducing
a `main()` function.

```python
from pcinput import getInteger
from sys import exit

while True:
    x = getInteger( "Enter number 1: " )
    if x == 0:
        break
    y = getInteger( "Enter number 2: " )
    if y == 0:
        break
    if (x < 0 or x > 1000) or (y < 0 or y > 1000):
        print( "The numbers should be between 0 and 1000" )
        continue
    if x%y == 0 or y%x == 0:
        print( "Error: the numbers cannot be dividers" )
        exit()
    print( "Multiplication of", x, "and", y, "gives", x * y )

print( "Goodbye!" )
```

### Assignment

Write a function `get_valid_number` that takes a prompt (`str`). The function
must use `getInteger` to keep asking for an integer using the given prompt,
until the user enters a value between 0 and 1000 (inclusive); for every value
outside that range, print `The numbers should be between 0 and 1000` before
asking again. The function must return the validated integer (`int`).

Rewrite the code above into a function `main` that takes no arguments, using
`get_valid_number` to fix the issue described above. Also get rid of the
`exit()` by using `return` instead.

### Example

```console?lang=python&prompt=>>>
>>> get_valid_number("Enter number 1: ")
Enter number 1: -42
The numbers should be between 0 and 1000
Enter number 1: 314
314

>>> main()
Enter number 1: -5
The numbers should be between 0 and 1000
Enter number 1: 250
Enter number 2: 999
Multiplication of 250 and 999 gives 249750
Enter number 1: 0
Goodbye!
```
