Recursion is a technique whereby a function calls itself. In a bit more
general sense, it is when a function makes calls in such a way that the
function itself is still being executed while it gets called again
(e.g., function `a()` calls function `b()`, which calls function `a()`
again).

This might sound weird when you first encounter it, but there is nothing
against a function calling other functions, and a function can call any
function that has been defined by the time that the call takes place.
And since a function is defined by the time its code gets executed, it
can call itself.

"But," one might say: "if a function calls itself, then it calls itself
again, and again, and again… Doesn't that mean it gets into an endless
process, similar to an endless loop?" The answer is that there is
certainly a danger, with sloppy coding, that a recursive function gets
into an endless loop, but recursive functions should be designed in such
a way that that does not happen.

There exist many problems for which recursion is the most elegant
solution. Therefore it is important that you are aware of the technique,
and know how and when to apply it... and its limitations.

![recursion](media/Recursion.png "recursion"){:width="80%"}

