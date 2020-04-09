In the IDLE shell you can type commands on the
IDLE prompt (`>>>`). Give the command `print(7/4)`. You will see that it
prints the answer $$1.75$$. Then give the command $$7/4$$ (i.e., without
`print`). Observe that it also prints the answer $$1.75$$.

The reason is that the IDLE shell will always display the result of a
command. The result of $$7/4$$ is $$1.75$$, and therefore it displays
$$1.75$$. The result of a `print` command is nothing, so the shell
displays nothing – however, the `print` command causes the display of
whatever is within the parentheses, which is the value resulting from
dividing $$7$$ by $$4$$, which is $$1.75$$. Therefore, in both cases you see
$$1.75$$, but one is the result of the use of the `print` command, while
the other is the result of the shell showing you the evaluation of a
calculation.

Now write a Python program that contains only the command $$7/4$$. Before
you run it, think about what you expect to happen when you run it. Will
the shell display $$1.75$$? Will it display nothing? Or will you see an
error?

Check if your expectation is correct.  
