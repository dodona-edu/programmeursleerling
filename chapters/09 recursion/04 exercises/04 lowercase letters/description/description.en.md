In the code below, I have implemented a
recursive implementation of asking the user for a string, in which only
lower case letters may be used. When someone enters a string with an
illegal character in it, a recursive call to the function itself will
ask for a new string. This looks like it avoids using the
loop-and-a-half to ask the user for new inputs on incorrect inputs.

### Assignment

While it is always a bad idea to place control over the depth of
recursive calls into a user's hands, this implementation actually is not
only bad, it is also quite wrong. Can you see what is wrong with it, and
how that is caused?

{:class="callout callout-info"}
> #### Tip
> It is not the `letter < 'a' or letter > 'z'`
expression, those comparisons are just fine.

{:class="callout callout-info"}
> #### Note
> Let me stress once more that the idea above is a *bad* one. You should not use recursion for commonplace problems that can just as well be solved by iterations. Recursion is for exceptional circumstances. Do not see this as an example of recursion, see it as an example of how not to use recursion! The main reason I put it here is that I sometimes observe students writing such code, and I want to make explicit that that is *not a good idea*!  
