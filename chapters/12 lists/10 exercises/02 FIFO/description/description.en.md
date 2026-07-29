A first-in-first-out (FIFO) structure, also called
a "queue," is a list that gets new elements added at the end, while
elements from the front are removed and processed. Write a program that
processes a queue. In a loop, ask the user for input. If the user just
presses the `Enter` key, the program ends. If the user enters anything
else, except for a single question mark (`?`), the program considers
what the user entered a new element and appends it to the queue. If the
user enters a single question mark, the program pops the first element
from the queue and displays it. You have to take into account that the
user might type a question mark even if the queue is empty.

### Assignment

Represent a queue as a list (`list`) of strings (`str`), and write the following three functions.

- Write a function `push` that takes a queue and an element. The function must add the given element at the end of the given queue, and must not return anything.

- Write a function `pop` that takes a queue. The function must remove the first element from the given queue and return it. If the given queue is empty, the function must leave the queue untouched and return `None`.

- Write a function `process` that takes a list (`list`) of strings (`str`), which stand for the successive lines the user enters. Starting from an empty queue, the function must process these lines one by one: an empty line ends the processing, a single question mark (`?`) pops the first element from the queue and prints it, and any other line is added at the end of the queue. If the user enters a question mark while the queue is empty, the function must print the message `The queue is empty.` instead.

### Example

```console?lang=python&prompt=>>>
>>> queue = ['apple', 'pear']
>>> push(queue, 'fig')
>>> queue
['apple', 'pear', 'fig']
>>> pop(queue)
'apple'
>>> queue
['pear', 'fig']
>>> process(['apple', 'pear', '?', 'fig', '?', '?', '?', '', 'plum'])
apple
pear
fig
The queue is empty.
```
