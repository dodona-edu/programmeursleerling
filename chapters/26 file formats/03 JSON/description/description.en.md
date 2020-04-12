JavaScript Object Notation (JSON) is a file format that is often used in
modern applications, in particular those that communicate via web
services. It is supported by many languages (JavaScript amongst them, of
course). It is similar to pickling in the sense that it stores in-memory
objects to files, retaining their structure. A difference with pickling
is that JSON files are in human-readable format.

The `json` module works equivalent to the `pickle` module, with a
`dump()` function that writes data structures to a file, and a `load()`
function to load data structures from a file. The file must be a text
file, and not a binary file.

```python
from json import dump, load

cheeseshop = [ ("Roquefort", 12, 15.23), 
    ("White Stilton", 25, 19.02), ("Cheddar", 5, 0.67) ]

fp = open( "pc_cheese.json", "w" )
dump( cheeseshop, fp )
fp.close()

fp = open( "pc_cheese.json", "r" )
buffer = load( fp )
fp.close()

print( type( buffer ) )
print( buffer )
```

Alternatives for `dump()` and `load()` are the functions `dumps()` and
`loads()`, which do not get a file argument. Instead, `dumps()` gets no
file argument at all, and just produces a string that contains the data
structure in JSON format, while `loads()` gets a string as argument
instead of a file, and loads the data structure from that string.

These functions can get many optional arguments that determine how
exactly the data will be stored; for instance, you can set the `indent=`
argument for `dump()` and `dumps()` to determine which indentation value
will be used, and you can use arguments to sort the data in the dump. If
you want to know more about this, consult the references.

A weakness of the `json` module is that it only supports the standard
Python data structures. If you want to use it to store instances of
classes of your own making, you have to find a way to convert your own
classes to standard Python structures. The `json` module offers special
`JSONencoder` and `JSONdecoder` classes to help you with that. It goes
too far to discuss these here.
