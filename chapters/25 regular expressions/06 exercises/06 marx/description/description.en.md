When scraping data from HTML pages,
you can often find the items you are interested in by looking for
mark-ups. Suppose that we have a page with data of persons, who have an
ID and a name. The ID is a nine-digit number, and has a marker `<id>` in
front of it, and a marker `</id>` after it. The name belonging to the ID
will follow immediately after the ID, and has a marker `<name>` in front
of it, and a marker `</name>` after it. Use a regular expression to
extract all the IDs and corresponding names from the text below, and
print them. There should be five of them.

```python
import re

text = "<html><head><title>List of persons with ids</title>\
</head><body>\
<p><id>123123123</id><name>Groucho Marx</name>\
<p><id>123123124</id><name>Harpo Marx</name>\
<p><id>123123125</id><name>Chico Marx</name>\
<randomcrap>Etaoin<id>Shrdlu</id>qwerty</name></randomcrap>\
<nocrap><p><id>123123126</id><name>Zeppo Marx</name></nocrap>\
<address>Chicago</address>\
<morerandomcrap><id>999999999</id>nonametobeseen!\
</morerandomcrap>\
<p><id>123123127</id><name>Gummo Marx</name>\
<note>Look him up on <a href=\"http://www.google.com\">\
Google.</a></note>\
</body></html>"
```
