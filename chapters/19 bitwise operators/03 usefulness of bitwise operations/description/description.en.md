Anything that you can do with bitwise operators, you can also do with
general calculations, with the advantage of general calculations that
they can do much more than bitwise operators. So what is the use of
bitwise operators?

Bitwise operations are incredibly fast. Much, much faster than regular
calculations. So should you use them when making calculations, when it
is opportune to do so? The answer is no, for two reasons:

-   Python is already smart enough to recognize that some calculations
    can be executed using bitwise operators, so it will make the
    conversion for you.

-   If you really want a fast program, you should not use Python at all.

Another use that is often mentioned, is that they facilitate storing
boolean values in a small storage space. For instance, if I have eight
booleans that I want to store, I can use a tuple of eight booleans,
which amounts to at least eight bytes of space, or encode all eight of
them in one byte using bitwise operators. However, in today's computers
space is of little concern, so only if you are talking about huge,
*huge* data collections you might get worried about space.

So what is the use of bitwise operators then? They are actually of
fairly little use, unless you have to create programs that need to work
"close to the machine." Occasionally you have to deal with data
structures that are most naturally handled using bitwise operators. They
may also help when you need to manipulate the content of binary files.

To give an example: colors are usually encoded as three bytes, for the
red, green, and blue channel. A color number is thus a three-byte
number. Bitwise operators are a natural way to distinguish the separate
color channels from a color number. Here is a function that does that:

```python
def getRGB( color ):
    blue = color & 255
    green = (color >> 8) & 255
    red = (color >> 16) & 255
    return red, green, blue
    
r, g, b = getRGB( 223567 )
print( "red={}, green={}, blue={}".format( r, g, b ) )
```

For someone who knows about color encoding, such a function reads well.
