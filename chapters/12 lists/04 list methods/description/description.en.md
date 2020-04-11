Python supports many methods to change lists or get information from
them. You do not need to import a module to use them. Since they are
methods, you call them using the syntax `<``list``>.<method>()`.

{:class="callout callout-warning"}
> #### Important
> Lists are mutable and these methods actually change the
> list! It is not as you are used to with string methods, where the
> methods create a new string, and return it, while the original string
> remains. Most list methods have an irrevocable effect on the list they
> work on. Usually they have no return value, and you do not need one
> either, as the purpose of the methods is to change the list.

### `append()`

`append()` attaches an item at the end of a list. You call the method
with the item you wish to add as argument.

```python
fruitlist = ["apple", "banana", "cherry", "durian"]
print( fruitlist )
fruitlist.append( "orange" )
print( fruitlist )
```

An alternative for using the `append()` method is to add a list with one
new element to the existing list with a $+$, and assign the resulting
list to the original list variable. However, the `append()` method is
preferable as it is more readable. `<``list``>.append(<element>)` is
equivalent to `<``list``>[len(<``list``>):] = [<element>]`, or simply
`<``list``> += [<element>]`.

### `extend()`

`extend()` makes a list longer by appending the elements of another list
at the end. You call the method with the list of which you want to add
the elements as argument.

```python
fruitlist = ["apple", "banana", "cherry", "durian"]
print( fruitlist )
fruitlist.extend( ["raspberry", "strawberry", "blueberry"] )
print( fruitlist )
```

Just as with the `append()` method, you can extend an existing list with
a new list by simply using the $+$ operator, and assigning the result to
the original list variable. And just as with the `append()` method, the
`extend()` method is preferable. `<``list``>.extend(<addlist>)` is
equivalent to `<``list``>[len(<``list``>):] = <addlist>`.

### `insert()`

`insert()` allows you to insert an element at a specific position in a
list. It is called with two arguments, the first being the index of the
location where you wish to insert the new element, and the second the
new element itself. To insert an element at the front of the list, you
can use index 0.

```python
fruitlist = ["apple", "banana", "cherry", "durian"]
print( fruitlist )
fruitlist.insert( 2, "orange" )
print( fruitlist )
```

`<``list``>.insert(<i>,<element>)` is equivalent to
`<``list``>[<i>:<i>] = [<element>]`.

### `remove()`

`remove()` allows you to remove an element from a list. The element you
wish to remove is given as argument. If the element occurs in the list
multiple times, only the first occurrence will be removed. If you try to
remove an element that is not on the list, a runtime error is generated.

```python
fruitlist = ["apple", "banana", "cherry", "banana", "durian"]
print( fruitlist )
fruitlist.remove( "banana" )
print( fruitlist )
```

### `pop()`

Like `remove()`, `pop()` removes an element from the list, but does so
by index. It has one optional argument, which is the index of the
element that you wish to remove. If you do not provide that argument,
`pop()` removes the last element from the list. If the index is beyond
the boundaries of the list, `pop()` generates a runtime error.

A major difference with `remove()` is that `pop()` actually has a return
value, namely the element that gets removed. This allows you to quickly
process all the elements of a list, while emptying the list at the same
time.

```python
fruitlist = ["apple", "banana", "cherry", "durian"]
print( fruitlist )
print( fruitlist.pop() )
print( fruitlist )
print( fruitlist.pop( 0 ) )
print( fruitlist )
```

### `del`

`del` is neither a method nor a function, but since it is often metioned
in one breath with `remove()` and `pop()`, I place it here. `del` is a
keyword that allows you to delete a list element, or list slice, by
index. It is similar to `pop()` in functionality, but does not have a
return value. Also, `pop()` cannot be used on slices. To remove one
element from a list, use `del <``list``>[<index>]`. To remove a slice,
use `del <``list``>[<index1>:<index2>]`.

```python
fruitlist = ["apple", "banana", "cherry", "banana", "durian"]
del fruitlist[3]
print( fruitlist )
```

### `index()`

`index()` returns the index of the first occurrence on the list of the
element that is given to `index()` as argument. A runtime error is
generated if the element is not found on the list.

```python
fruitlist = ["apple", "banana", "cherry", "banana", "durian"]
print( fruitlist.index( "banana" ) )
```

### `count()`

`count()` returns an integer that indicates how often the element that
is passed to it as an argument occurs in the list.

```python
fruitlist = ["apple", "banana", "cherry", "banana", "durian"]
print( fruitlist.count( "banana" ) )
```

### `sort()`

`sort()` sorts the elements of the list, from low to high. If the
elements of the list are strings, it does an alphabetical sort. If the
elements are numbers, it does a numeric sort. If the elements are mixed,
it generates a runtime error, unless certain arguments are given.

```python
fruitlist = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
fruitlist.sort()
print( fruitlist )

numlist = [314, 315, 642, 246, 129, 999]
numlist.sort()
print( numlist )
```

To do a reverse sort (for instance, sorting numerical items from high to
low, or sorting strings alphabetically from `"z"` to `"a"`), you can add
an argument `reverse=<boolean>`.

```python
fruitlist = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
fruitlist.sort( reverse=True )
print( fruitlist )
```

Another argument that you can give `sort()` is a key. You have to
provide this argument as `<``list``>.sort( key=<key> )`, whereby `<key>`
is a function that takes one argument (the element that is to be sorted)
and returns a value that is used as key. A typical use for the key
argument is if you want to sort a list of strings, but want to do the
sorting case-insensitively. So as key you want to use the elements, but
in lower case, i.e., you want to apply the function `str.lower()` to the
element. You call the `sort()` method as in the following example:

```python
fruitlist = ["apple", "Strawberry", "banana", "raspberry", "CHERRY", "banana", "durian", "blueberry"]
fruitlist.sort() 
print( fruitlist )
fruitlist.sort( key=str.lower ) # case-insensitive sort
print( fruitlist )
```

Note that for the key argument, you do not place parentheses after the
function name. This is not a function call, it is an argument that tells
Python which function to use to generate the key. You can write your own
function to be used as key. For example, in the code below, `numlist` is
sorted with the digits reversed:

```python
def revertdigits( item ):
    return (item%10)*100 + (int(item/10)%10)*10 + int(item/100)

numlist = [314, 315, 642, 246, 129, 999]
numlist.sort( key=revertdigits )
print( numlist )
```

Here is another example, that sorts a list of strings by length, then
alphabetical order:

```python
def len_alphabetical( element ):
    return len( element ), element 

fruitlist = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
fruitlist.sort( key=len_alphabetical )
print( fruitlist )
```

Note that the `len\_alphabetical()` function returns a tuple. When two
tuples are compared, first the first elements of both tuples are
compared, and if they are equal, the second elements are compared.

At this point I can give a typical example of the use of "anonymous
functions," which I introduced in Chapter
<a href="#ch:functions" data-reference-type="ref" data-reference="ch:functions">9</a>.
Using an anonymous function to specify the key for the `sort()` method
keeps the code for the key next to where you call the `sort()`, instead
of elsewhere in the program. This may improve readability.

```python
fruitlist = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
fruitlist.sort( key=lambda x: (len(x),x) )
print( fruitlist )
```

### `reverse()`

`reverse()` simply puts the elements of the list in reverse order.

```python
fruitlist = ["apple","strawberry","banana","raspberry","durian"]
fruitlist.reverse()
print( fruitlist )
```

### Practice

Write a program that asks the user to enter some data, for instance the
names of their friends. When the user wants to stop providing inputs, he
just presses `Enter`. The program then displays an alphabetically sorted
list of the data items entered. Do not just print the list, but print
each item separately, on a different line.

Sort a list of numbers using their absolute values; use the `abs()`
function as key.

Count how often each letter occurs in a string (case-insensitively). You
can ignore every character that is not a letter. Store the counts in a
list of 26 items that all start at zero. Print the resulting counts. As
index you can use `ord(letter) - ord("a")`, where letter is a lower case
letter (the `ord()` function is explained in Chapter
<a href="#ch:strings" data-reference-type="ref" data-reference="ch:strings">11</a>).
