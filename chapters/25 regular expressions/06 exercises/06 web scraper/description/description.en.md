When scraping data from HTML pages, you can often find the items you are interested in by looking for mark-ups. Suppose that we have a page with data of persons, who have an ID and a name. The ID is a nine-digit number, and has a marker `<id>` in front of it, and a marker `</id>` after it. The name belonging to the ID will follow immediately after the ID, and has a marker `<name>` in front of it, and a marker `</name>` after it.

### Assignment

Write a function `webscraper` that takes the location of a HTML file (`str`). The function must return a `list` containing all data of persons in the given text file. The data of a person is represented as a `tuple` containing the ID (`int`) and the name (`str`) of the person.

### Example

In the following interactive session we assume the text file [`data.html`](media/data/data.html){:target="_blank"} to be located in the current directory.

```console?lang=python&prompt=>>>
>>> webscraper('data.html')
[(123123123, 'Groucho Marx'), (123123124, 'Harpo Marx'), (123123125, 'Chico Marx'), (123123126, 'Zeppo Marx'), (123123127, 'Gummo Marx')]
```
