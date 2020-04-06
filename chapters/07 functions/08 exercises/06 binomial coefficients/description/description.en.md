In statistics, the binomial coefficient
indexed by `n` and `k` (often expressed as "n over k," whereby `n` must
be bigger than or equal to `k`) is calculated as $n!/(k!*(n-k)!)$,
whereby $n!$ indicates the factorial of `n`. As I explained in Chapter
<a href="#ch:iterations" data-reference-type="ref" data-reference="ch:iterations">8</a>:
the factorial of a positive integer is that integer, multiplied by all
positive integers that are lower (excluding zero). You write the
factorial as the number with an exclamation mark after it. E.g., the
factorial of 5 is $5! = 5 * 4 * 3 * 2 * 1 = 120$. If you did all the
exercises until now, you wrote some code for this. Write a function that
calculates the binomial coefficient for its two parameters, and returns
the value. Write the code in such a way that it can be used as a module
by another program (i.e., put the tests of your program in a `main()`
function that is called as explained above).
