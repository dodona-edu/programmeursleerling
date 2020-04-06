In Chapter
<a href="#ch:iterations" data-reference-type="ref" data-reference="ch:iterations">8</a>,
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
