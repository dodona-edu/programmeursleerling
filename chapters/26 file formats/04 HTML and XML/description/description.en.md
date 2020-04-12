HTML and XML are standard formats that are used to display information
on webpages. They consist of readable text files, with many instructions
on formatting. It is a common task for data miners to "scrape" data from
webpages. You can use regular expressions for that, but if the webpages
are reasonably well-formatted, the "Beautiful Soup" module may help you
out.

The Beautiful Soup module is named `bs4` in Python (naturally, `bs3`
came before it, and it may get more updates later). It contains the
`BeautifulSoup` class that you can use to load and interpret HTML and
XML files. `bs4` is not part of the standard Python package; you have to
install it separately, which is quite a hassle, unless you use a tool
called `pip` which comes standard with Python 3.

There are alternative modules that can ease the pain of web scraping for
you, notably `lxml`, but Beautiful Soup seems to be the most popular.

Since all such modules require separate installations, I will not
discuss them here. I only wish to indicate that if you need to do web
scraping (and it is likely you have to do that at some point), you
should check out some of the standard tools available for that before
you delve into eccentric regular expression-design.
