Create a program that asks the user
for numbers, until the user enters zero. It then prints the mean,
median, and mode of these numbers. The `statistics` module can be used
for the mean and median; however, for the mode, print all those numbers
that have the highest count, even if that entails that you print more
than one number. By definition, for a number to be the mode it must
occur at least twice; so if every number only occurs once, there is no
mode. Hint: Consider using the `Counter` class to construct the mode.

### Assignment

Write a function `mode` that takes a list of integers and returns a sorted list of the number(s) that occur most often. A number only counts as a mode if it occurs at least twice; if every number in the list occurs only once, or the list is empty, there is no mode and the function must return an empty list. If multiple numbers are tied for the highest count, return all of them, sorted from low to high.

Use this function in your program: keep asking the user for numbers until they enter 0, then print the mean, median, and mode of the numbers that were entered (not counting the final 0). The `statistics` module can be used for the mean and median.

### Example

```console?lang=python&prompt=>>>
>>> mode([4, 8, 15, 16, 23, 8, 4, 8])
[8]
>>> mode([7, 2, 9, 2, 9, 3])
[2, 9]
>>> mode([5, 10, 15])
[]
```
