How often does a letter appear in a text?

### Assignment

Write a function `letterfrequenties` that takes the locations of four text files (`str`). For each letter in the alphabet, the function must compute the frequency of the letter in each of the first three text files. This letter frequency is computed as the number of occurrences of a letter in a text file, divided by the total number of letters in the text file. This is done without making a distinction between uppercase and lowercase letters.

The function must write a CSV-file to the fourth text file. This CSV file must contain a record with four fields for each letter in the alphabet (in alphabetic order): **i**) the letter (lowercase), **ii**) the frequency of the letter in the first text file, **iii**) the frequency of the letter in the second text file and **iv**) the frequency of the letter in the third text file. All frequencies must be written with five decimals (rounded).

### Example

In the following interactive session we assume the text files [`data_a.txt`](media/data/data_a.txt){:target="_blank"}, [`data_b.txt`](media/data/data_b.txt){:target="_blank"} and [`data_c.txt`](media/data/data_c.txt){:target="_blank"} to be located in the current directory.

```console?lang=python&prompt=>>>
>>> letter_frequencies('data_a.txt', 'data_b.txt', 'data_c.txt', 'data.csv')
>>> print(open('data.csv').read(), end='')
a,0.06081,0.08505,0.10141
b,0.00000,0.04527,0.01127
c,0.16216,0.02332,0.01972
d,0.10135,0.04527,0.01972
e,0.02027,0.11111,0.11268
f,0.01351,0.01372,0.02535
g,0.00000,0.02881,0.01408
h,0.10811,0.08368,0.07606
i,0.01351,0.05075,0.03944
j,0.00000,0.01235,0.00000
k,0.06081,0.01097,0.00282
l,0.04730,0.04115,0.03944
m,0.02027,0.03567,0.05070
n,0.00676,0.04938,0.07606
o,0.14865,0.07407,0.10423
p,0.00000,0.00412,0.00845
q,0.00000,0.00000,0.00000
r,0.00000,0.04664,0.05915
s,0.02703,0.05213,0.04225
t,0.00000,0.09191,0.11549
u,0.12838,0.02881,0.02254
v,0.00000,0.00823,0.00000
w,0.08108,0.03292,0.03380
x,0.00000,0.00137,0.00000
y,0.00000,0.02332,0.02535
z,0.00000,0.00000,0.00000
```

{:class="callout callout-info"}
> #### Note
> As the output file is a CSV file, you should also be able to load it in a 
> spreadsheet program. A quick check to see if you did things correctly is that 
> all of the fractions must be between zero and 1, and the fraction for the 
> letter `e` should be highest for the last two files (but not so much for the 
> first file). If you would use longer files which are all in the same language, 
> you would also find that the fractions are usually more or less in each 
> others' neighborhood. 
