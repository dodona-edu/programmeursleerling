The `urllib` module allows you to access web pages in the same way that
you access files. There are two modules of main interest:
`urllib.request` contains functions to access Internet content, and
`urllib.error` contains definition for exceptions that can be raised.
You can also use `urllib` to communicate with webpages; if you want to
do so, you need to study the `urllib.parse` module. For now, I only give
a simple example in which you want to open a webpage and read its
contents.

```python
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from sys import exit

try:
    u = urlopen( "http://www.python.org" )
except HTTPError as e:
    print( "HTTP Error", e )
    sys.exit()
except URLError as e:
    print( "URL error", e )
    sys.exit()

for i in range( 5 ):
    text = u.readline()
    print( text )

u.close()
```

Note that from `urllib` only `urlopen` needs to be imported. Once you
have opened a web address, it is returned as a file handle, so you can
use the regular file methods on it.
