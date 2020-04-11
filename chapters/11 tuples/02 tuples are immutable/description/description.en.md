Just like strings, tuples are immutable. This means that you cannot
assign a new value to one element of a tuple. The example below will
produce a runtime error when run.

```python
t1 = ("apple", "banana", "cherry", "durian")
t1[0] = "orange"
```
