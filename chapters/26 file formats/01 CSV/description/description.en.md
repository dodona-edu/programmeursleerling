Comma-Separated Values (CSV) is the most common text file format that is
used for importing and exporting data to and from spreadsheets and
databases. The general format says that each line contains one record (a
record is a complete entity), listing each of the fields of the record
in a specific order, separating the fields by commas. The first line of
the file may or may not consist of names for the fields in the CSV file.

The code below loads and displays the contents of a typical CSV file.
Appendix
<a href="#ch:testtextfiles" data-reference-type="ref" data-reference="ch:testtextfiles">33</a>
explains how to get this CSV file.

```python
fp = open( "pc_inventory.csv" )
print( fp.read().strip() )
fp.close()
```

Unfortunately, the CSV format is not standardized, and different
software packages tend to use slightly different implementations of CSV
files. However, over the years the different conventions used by the
major software packages have converged to something of a standard, that
is implemented in the Python `csv` module. The module supports
"dialects" of CSV formats to handle files from different sources.

Instead of using the `csv` module, if you have to deal with an excentric
CSV format that the module does not support, you can try to design your
own interpretation of lines of the file using regular expressions. You
can also try to design your own dialect. Neither option is very
appealing.

### CSV `reader()`

The `csv` module contains a `reader()` function that provides access to
a CSV file. The `reader()` function gets a file handle as argument, and
returns an iterator that allows you to get the lines from the file, as a
list with each of the fields as an element of the list. You should leave
the file open while accessing it with `reader()`.

```python
from csv import reader

fp = open( "pc_inventory.csv", newline='' )
csvreader = reader( fp )
for line in csvreader:
    print( line )
fp.close()
```

The Python documentation recommends that if you use `reader()` on a file
(and that is what you usually do), you specify a `newline=''` argument
as extra argument when opening the file (I did this in the code above).
This is necessary in case some of the text fields in the CSV file
contain newline characters.

`reader()` takes extra arguments too. Common ones are
`delimiter=<character>`, which indicates the `<character>` which is
placed between different fields (default is the comma), and
`quotechar=<character>`, which indicates which `<character>` is used to
enclose strings with (default is the double quote).

### CSV `writer()`

Writing a CSV file is just a little bit harder than reading one. You
create a file handle to a file that you open for writing (`"w"` mode),
and use it as an argument when you call the `writer()` function from the
`csv` module. The object that is returned from the `writer()` call has a
method `writerow()` that you can call with a list of fields, that it
then writes to the output file in CSV format.

The call to `writer()` can get the same arguments as the call to
`reader()` can get, including specifying a `delimiter` and a
`quotechar`. You can also supply a `quoting=<quotemethod>` argument,
that supports the following methods of quoting:

-   `csv.QUOTE_ALL`, which encloses every field in quotation characters

-   `csv.QUOTE_MINIMAL`, which only encloses fields in quotation
    characters if it is absolutely necessary (this is the default)

-   `csv.QUOTE_NONNUMERIC`, which encloses fields in quotation
    characters if they are not integers or floats

-   `csv.QUOTE_NONE`, which encloses no fields in quotation characters

Enclosing a string within quotation characters is generally only needed
if the string contains exceptional characters, such as newlines or the
character that is used as delimiter.

```python
from csv import writer

fp = open( "pc_writetest.csv", "w", newline='' )
csvwriter = writer( fp )
csvwriter.writerow( ["MOVIE", "RATING"] )
csvwriter.writerow( ["Monty Python and the Holy Grail", 8] )
csvwriter.writerow( ["Monty Python's Life of Brian", 8.5] )
csvwriter.writerow( ["Monty Python's Meaning of Life", 7] )
fp.close()
```

After using the code above to create the file "pc\_writetest.csv," open
it and use `reader()` to list its contents.
