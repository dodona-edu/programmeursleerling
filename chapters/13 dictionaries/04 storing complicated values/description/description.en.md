Until now I only considered the case in which a dictionary stores a
single value of a simple data type. However, it is possible to store
much more complex values in dictionaries. Values can be arbitrary Python
objects. For example, you can store a list with each key. Below a
dictionary is used to store the students who are following a course. The
course is identified by its course number, while the students are
identified by their student numbers.

```python
courses = {
    '880254':['u123456', 'u383213', 'u234178'], 
    '822177':['u123456', 'u223416', 'u234178'], 
    '822164':['u123456', 'u223416', 'u383213', 'u234178']}

for c in courses:
    print( c )
    for s in courses[c]:
        print( s, end=" " )
    print()
```

Suppose that you do not only want to store the student numbers for a
course number, but also the name of the course, the ECTS value of the
course, and for each student number also the grade. You can do that (for
example) by storing the value for a course number as a dictionary, with
three keys, namely `"name"`, `"ects"`, and `"students"`. The value for
`"name"` is the course name as a string, the value for `"ects"` is the
ECTS as an integer, and the value for `"students"` is another
dictionary, which contains student numbers as keys and grades as values.

```python
courses = {
    '880254': { "name":"RS: Data Processing", "ects":3, 
        "students":{'u123456':8, 'u383213':7.5, 'u234178':6} }, 
    '822177': { "name":"Understanding Intelligence", "ects":6,
        "students":{'u123456':5, 'u223416':7, 'u234178':9} }, 
    '822164': { "name":"Computer Games", "ects":6,
        "students":{'u383213':6, 'u234178':4} } }

for c in courses:
    print( "{}: {} ({})".format( c, courses[c]["name"], 
        courses[c]["ects"] ) )
    for s in courses[c]["students"]:
        print( "{}: {}".format( s, courses[c]["students"][s] ) )
    print()
```

Data structures can become a lot more complex than this if you want.
However, if you are really considering designing Python programs for
data structures like this, you should at least investigate object
orientation first (Chapter
<a href="#ch:objectorientation" data-reference-type="ref" data-reference="ch:objectorientation">21</a>
and onward) and probably do a separate course on databases.
