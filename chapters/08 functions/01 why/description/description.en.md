Why would you want to create a function? There are several different reasons
why you want to have a function:

-   You may need a particular functionality for your code that you want
    to develop in independence of the rest of the code. If you put such
    a functionality in a function, that means that after developing and
    testing the functionality you can use it without thinking about it
    anymore.

-   You may need a particular functionality that returns in different
    places in your code, and rather than copy it to all these places,
    you write a function for it which you call in all these places.

-   You may need a particular functionality in your code that you need
    to control using parameters. If you put it in a function, the
    parameters become clearer and the code becomes more readable and
    easy to maintain.

-   Your program may just be getting too long to keep a solid grasp on
    its contents, and you feel you can improve readability and
    maintainability by splitting off inherently connected blocks into
    functions.

-   You may have problems solving a big problem in one go, and decide to
    divide it into sub-problems (which is usually a good idea). You can
    now create a function for each of these sub-problems, and by
    connecting them together, solve the big problem.

-   Your program may contain deeply nested conditions or loops, and
    would benefit enormously as far as readability is concerned by
    moving some of the deeper nestings into functions.

-   You may want to re-use code in different programs, and functions are
    a good way to transfer code between programs.

-   You may want to release some of your code to other programmers, and
    functions are, again, a good way to do that.

In general, the advantage of functions is that they provide a means to
effectuate:

-   *Encapsulation*: Wrapping up a piece of useful code in such a way
    that it can be used without knowledge of the specifics

-   *Generalization*: Making a piece of code useful for a variety of
    circumstances by controlling it via parameters

-   *Manageability*: Dividing a complex program into easy-to-manage
    chunks

-   *Maintainability*: Using meaningful names and logical wrappings to
    make a program better readable and understandable

-   *Reusability*: Facilitating the transfer of functionalities between
    programs

-   *Recursion*: Allowing the use of a technique called "recursion,"
    which is the topic of Chapter
    <a href="#ch:recursion" data-reference-type="ref" data-reference="ch:recursion">10</a>.
