A core property of strings is that they are immutable. This means that
they cannot be changed. For instance, you cannot change a character of a
string by assigning a new value to it. As a demonstration, the following
code leads to a runtime error if you try to run it:

```python
fruit = "oringe"
fruit[2] = "a"  # Runtime error!
print( fruit )
```

If you want to make a change to a string, you have to create a new
string that contains the change; you can then assign the new string to
the existing variable if you want. For instance:

```python
fruit = "oringe"
fruit = fruit[:2] + "a" + fruit[3:]
print( fruit )
```

The reasons for why strings are immutable are beyond the scope of this
book. Just remember that if you want to modify a string you need to
overwrite the entire string, and you cannot modify individual indices.
