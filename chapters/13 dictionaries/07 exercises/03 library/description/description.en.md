A library contains books. Books have a
writer, identified by last name and first name. Books also have a title.
Books also have a location number that identifies where they can be
found in the library. Librarians want to be able to locate a specific
book if they know writer and title, and they want to be able to list all
the books that they have of a specific writer. What data structure would
you use to store the books?

<details markdown="1">
<summary>Answer</summary>

Use a dictionary (`dict`) that maps each writer onto another dictionary
(`dict`), holding the titles of that writer's books and their location
numbers. Represent the writer itself as a `tuple` with the last name and
the first name: a `tuple` is immutable, so it can be used as a key of a
dictionary, which a `list` cannot.

That covers both things the librarians want. To locate a single book, you
look up the writer and then the title. To list everything the library has
of a writer, you take the keys of that writer's inner dictionary.

</details>

### Assignment

**Data about the books of a library** is represented as a `list` of books, with each book represented as a `tuple` containing four elements: *i*) the last name of the writer (`str`), *ii*) the first name of the writer (`str`), *iii*) the title of the book (`str`) and *iv*) the location number of the book (`int`). Your task:

- Write a function `list2dict` that takes data about the books of a library. The function must return a dictionary (`dict`) that maps the writer (`tuple` containing the last name and the first name of the writer) of each book onto a dictionary (`dict`) that maps the title (`str`) of each book of that writer onto the location number (`int`) of that book.

- Write a function `location` that takes a dictionary (`dict`) formatted as the dictionaries returned by the function `list2dict`, followed by the last name (`str`) of a writer, the first name (`str`) of that writer and the title (`str`) of a book. The function must return the location number (`int`) of that book, or `None` if the library does not have that book.

- Write a function `titles` that takes a dictionary (`dict`) formatted as the dictionaries returned by the function `list2dict`, followed by the last name (`str`) and the first name (`str`) of a writer. The function must return the sorted list (`list`) of titles (`str`) of the books that the library has of that writer. This must be an empty list if the library has no books of that writer.

### Example

```console?lang=python&prompt=>>>
>>> books = [
...     ('Adams', 'Douglas', "The Hitchhiker's Guide to the Galaxy", 42),
...     ('Adams', 'Douglas', 'The Restaurant at the End of the Universe', 43),
...     ('Adams', 'Douglas', 'Life, the Universe and Everything', 44),
...     ('Rowling', 'Joanne', "Harry Potter and the Philosopher's Stone", 271),
...     ('Rowling', 'Joanne', 'Harry Potter and the Chamber of Secrets', 272),
...     ('Tolkien', 'John', 'The Hobbit', 137),
...     ('Spronck', 'Pieter', "The Coder's Apprentice", 512),
... ]
>>> library = list2dict(books)
>>> library[('Tolkien', 'John')]
{'The Hobbit': 137}
>>> library[('Rowling', 'Joanne')]
{"Harry Potter and the Philosopher's Stone": 271, 'Harry Potter and the Chamber of Secrets': 272}
>>> location(library, 'Adams', 'Douglas', 'Life, the Universe and Everything')
44
>>> location(library, 'Adams', 'Douglas', 'The Long Dark Tea-Time of the Soul') is None
True
>>> titles(library, 'Adams', 'Douglas')
['Life, the Universe and Everything', "The Hitchhiker's Guide to the Galaxy", 'The Restaurant at the End of the Universe']
>>> titles(library, 'Pratchett', 'Terry')
[]
```
