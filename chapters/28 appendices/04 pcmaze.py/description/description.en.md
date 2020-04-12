In Chapter
<a href="#ch:recursion" data-reference-type="ref" data-reference="ch:recursion">10</a>
an example of searching a maze is presented. In that example a module
`pcmaze` is used, that I wrote for this book. The module contains a
specific maze, and functions to access features of the maze. To create
the module, download it from <http://www.spronck.net/pythonbook>{:target="_blank"}, or
copy the code below to a file called "pcmaze.py," and make sure that it
is located in same folder where you keep the files with your own code.

```python
def connected( x, y ):
    if x > y:
        return connected( y, x )
    if (x,y) in ((1,5),(2,3),(3,7),(4,8),(5,6),(5,9),(6,7),
        (8,12),(9,10),(9,13),(10,11),(10,14),(11,12),(11,15),
        (15,16)):
        return True
    return False
    
def entrance():
    return 1
    
def exit():
    return 16
```
