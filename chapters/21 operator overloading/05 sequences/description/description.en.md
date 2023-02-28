A special kind of class is the sequence class. You have seen several
sequence classes, namely tuples, lists, dictionaries, and sets. Such
classes contain a sequence of elements, that can be accessed using
indices or keys. You can create such classes yourself, by overloading
several methods that support changing or getting information on the
elements of the class.

-   `__len__()` implements the `len()` function, which should return an
    integer that indicates the number of elements in the object.

-   `__getitem__()` implements returning the element with the key (or
    index) that is supplied as argument. This method is called when the
    object is referred to with a value between square brackets after it,
    e.g., `x[key]` with `x` the object and `key` the key or index of the
    element. If `key` is an index and the index is not appropriately
    referring to an object, then you are supposed to raise an
    `IndexError` (see Chapter
    18).
    If `key` is something else (as with, for instance, a dictionary) and
    it is not appropriately referring to an object, then you are
    supposed to raise a `KeyError`. When `key` is an index, for a
    complete implementation it should also support slices (implemented
    as so-called slice objects).

-   `__setitem__()` implements assigning a value to an element of the
    object which has the key or index that is given as argument, and the
    value as second argument. This method is called when a value is
    assigned to the object with a key or index value between square
    brackets after it, e.g., `x[key] = value`.

-   `__delitem__()` implements removing from the object the element that
    has the key or index that is given as argument, when the `del`
    keyword is used, e.g., `del x[key]`.

-   `__missing__()` is called by `__getitem__()`, with the key or index
    as argument, when the key or index is not referring to an element
    found in the object. This method is used in particular by subclasses
    of the Python dictionary.

-   `__contains__()` should be given an item (and not a key or index) as
    argument, and returns `True` if the item is found in object, and
    `False` otherwise. It is called when the `in` keyword is used to
    test for the existence of an item.

To demonstrate how these methods work, I have implemented a sequence
class that implements a Mesostic Puzzle. In Dutch, such puzzles are
known as "Filippines," but outside The Benelux they are not well known.
The puzzle consists of a list of questions, each of which is answered by
one word. Of each answer, one letter is indicated as "special." The
special letters, in order of the questions, provide the solution to the
puzzle.

I have defined each of the words for the puzzle as an instance of the
class `MesosticWord`, which consists of the answer, the index of the
special letter in the answer, and the question. The class `Mesostic` is
the complete puzzle, i.e., it is a sequence of `MesosticWord`s. I
implemented the `__len__()`, `__getitem__()`, `__setitem__()`, and
`__delitem__()` methods (the last two are not actually used in the
code).

I also implemented two more methods, which demonstrate how the
overloaded methods manage to do their job. `display()` displays the
puzzle, and uses thereby the `len()` function and indices on the puzzle
object itself. `solution()` displays the solution, also using `len()`
and indices.

```python
class MesosticWord:
    def __init__( self,  word, index, question ):
        self.word = word
        self.index = index
        self.question = question

class Mesostic:
    def __init__( self, name, words ):
        self.name, self.words = name, words
    def __len__( self ):
        return len( self.words )
    def __getitem__( self, n ):
        return self.words[n]
    def __setitem__( self, n, value ):
        self.words[n] = value
    def __delitem__( self, n ):
        del self.words[n]
    def display( self ):
        print( self.name )
        for i in range( len( self ) ):
            print( "{}. {}".format( i+1, self[i].question ),
                end = "  " )
            for j in range( len( self[i].word ) ):
                if j == self[i].index:
                    print( "* ", end="" )
                else:
                    print( "_ ", end="" )
            print()
    def solution( self ):
        s = ""
        for i in range( len( self ) ):
            s += self[i].word[self[i].index]
        return s

puzzle = Mesostic(
    "The Monty Python and the Holy Grail Mesostic Puzzle",
    [ MesosticWord( "ANTHRAX", 5,
          "Sir Galahad's tale took place in the Castle" ),
      MesosticWord( "PERIL", 2,
          "Sir Robin was thrown into the Gorge of Eternal" ),
      MesosticWord( "RABBIT", 5,
          "Sir Bors was killed by a" ),
      MesosticWord( "SHRUBBERY", 1,
          "The Knights of Ni!'s first demand was to get a" ),
      MesosticWord( "COCONUT", 5,
          "A horse can be replaced by a" ),
      MesosticWord( "MINSTRELS", 5,
          "They were forced to eat Robin's" ) ] )

puzzle.display()
```

Note: It would have been nicer if the stars, which indicate the special
letters, were printed in a column. However, depending on the editor that
you use, the display format does not always use a fixed letter width, so
it is hard to organize that. You may implement a solution for this on
your own, if you like (it is not relevant for the theme of the chapter).

Another important method that you can implement for sequence classes is
`__iter__()`. This one will be discussed in Chapter
24.

When implementing a sequence class, you should also consider creating a
suitable implementation of the `__add__()` method, and possibly a
suitable implementation of the `__mul__()` method.

A `Sentence` is a list of words. A basic `Sentence` class is given
below. Implement `__len__()`, `__getitem__()`, `__setitem__()`, and
`__contains__()` methods for this class.

```python
class Sentence:
    def __init__( self, words ):
        self.words = words
    def __repr__( self ):
        return " ".join( self.words )

s = Sentence( [ "There", "is", "only", "one", "thing", "worse",
"than", "being", "talked", "about",
"and", "that", "is", "not", "being", "talked", "about" ] )
print( s )
print( len( s ) )
print( s[5] )
s[5] = "better"
print( "being" in s )
```
