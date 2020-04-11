If you assign a variable that contains a list to another variable, you
might expect that you create a copy of the list in the second variable.
But you are not doing that. You are actually creating an *alias* for the
list, i.e., a new variable that is referring to the same list. This
means that the new variable can be treated as a list, but any change
that you make to the list it refers to, is visible in the original list
variable, and vice versa. They are not different lists.

```python
fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
print( fruitlist )
print( newfruitlist )
newfruitlist[2] = "orange"
print( fruitlist )
print( newfruitlist )
```

Every variable in Python has an identification number. You can see it
with the `id()` function. The ID number indicates which memory spot the
variable refers to. For an alias of a list, the ID is the same as for
the original list.

```python
fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
print( id( fruitlist ) )
print( id( newfruitlist ) )
```

If you want to create a copy of a list, you can do so using a little
trick. Instead of using `<newlist> = <oldlist>`, you use the command
`<newlist> = <oldlist>[:]`.

```python
fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
verynewfruitlist = fruitlist[:]

print( id( fruitlist ) )
print( id( newfruitlist ) )
print( id( verynewfruitlist ) )

fruitlist[2] = "orange"
print( fruitlist )
print( newfruitlist )
print( verynewfruitlist )
```

### `is`

The keyword `is` is introduced to compare the identities of two
variables.

```python
fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
verynewfruitlist = fruitlist[:]

print( fruitlist is newfruitlist )
print( fruitlist is verynewfruitlist )
print( newfruitlist is verynewfruitlist )
```

As you can see, the keyword `is` manages to determine that `fruitlist`
and `newfruitlist` are aliases, but that `verynewfruitlist` is not the
same list. If you compare them with the $==$ operator, the results are
not the same as comparing them with `is`:

```python
fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
verynewfruitlist = fruitlist[:]

print( fruitlist == newfruitlist )
print( fruitlist == verynewfruitlist )
print( newfruitlist == verynewfruitlist )
```

The $==$ operator actually compares the contents of the lists, so it
returns `True` for all comparisons. For data types for which $==$ is not
defined, it executes an identity comparison, but for lists it has been
defined as a comparison of the contents. I will return to this topic
when discussing "operator overloading" in Chapter
<a href="#ch:operatoroverloading" data-reference-type="ref" data-reference="ch:operatoroverloading">22</a>.

### Shallow vs. deep copies

If (some of) the items of your list are lists themselves (or other
mutable data structures which are introduced in the next chapters), you
may get problems if you copy the list using the
`<newlist> = <oldlist>[:]` syntax. The reason is that such a copy is a
"shallow copy," which means that it copies each of the elements of the
list with a regular assignment, which entails that the items in the list
that are lists themselves become aliases of the items on the original
list.

```python
numlist = [ 1, 2, [3, 4] ]
copylist = numlist[:]

numlist[0] = 5
numlist[2][0] = 6
print( numlist )
print( copylist )
```

In the code above, you can see that the assignment `numlist[0] = 5` only
has an effect on `numlist`, as `copylist` contains a copy of `numlist`.
However, since this is a shallow copy, the assignment to `numlist[2][0]`
has an effect on both lists, as the sublist `[3, 4]` is stored in
`copylist` as an alias.

If you want to create a "deep copy" of a list (i.e., a copy that also
contains true copies of all mutable substructures of the list, which in
turn contain true copies of all their mutable substructures, etcetera),
then you can use the `copy` module for that. The `deepcopy()` function
from the `copy` module allows you to create deep copies of any mutable
data structure.

```python
from copy import deepcopy

numlist = [ 1, 2, [3, 4] ]
copylist = deepcopy( numlist )

numlist[0] = 5
numlist[2][0] = 6
print( numlist )
print( copylist )
```

Note that the `copy` module also contains a function `copy()` that makes
shallow copies. If you wonder why that function is included as you can
easily create shallow copies of lists with the
`<newlist> = <oldlist>[:]` command: the `copy` module not only works for
lists, but for any mutable data structure. Not for all such data
structures there exist shortcuts to create shallow copies.

### Passing lists as arguments

When you pass a list as an argument to a function, this is a "pass by
reference." The parameter that the function has access to will be an
alias for the list that you pass. This means that a function that you
pass a list to, can actually change the contents of the list.

This is important, so I repeat it: when you pass a mutable data
structure to a function, this is a "pass by reference," meaning that the
data structure is passed as an alias and the function can change the
contents of the data structure.

You have to know whether a function that you pass a list to will or will
not change the list. If you do not want the function to change the list,
and you do not know if it will, you best pass a deep copy of the list to
the function.

```python
def changelist( x ):
    if len( x ) > 0:
        x[0] = "CHANGE!"

fruitlist = ["apple", "banana", "cherry", "durian"]
changelist( fruitlist )
print( fruitlist )
```

The reason that a list is "passed by reference" and not "by value" is
that technically, every argument that is passed to a function must be
stored in the computer in a specific block of memory that is part of the
processor. This is called the "stack," and it is pretty limited in size.
Since lists can be really long, allowing a program to place a list on
the stack would cause all kinds of annoying runtime errors. In Python,
as in most other programming languages, for the most part only basic
data types (such as integers, floats, and strings) are passed by value.
