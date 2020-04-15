"""
>>> print(open('data.txt', 'r').read(), end='')
How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood.
>>> vowel_removal('data.txt', 'copy.txt')
(190, 135)
>>> print(open('copy.txt', 'r').read(), end='')
Hw mch wd wld  wdchck chck
f  wdchck cld chck wd?
H wld chck, h wld, s mch s h cld,
nd chck s mch s  wdchck wld
f  wdchck cld chck wd.
"""

def vowel_removal(src_file, dest_file):

    characters_src = 0
    characters_dest = 0

    with open(src_file, 'r') as src:
        with open(dest_file, 'w') as dest:
            for line in src:
                characters_src += len(line)
                line = ''.join(
                    character for character in line
                    if character.lower() not in 'aeiou'
                )
                characters_dest += len(line)
                print(line, file=dest, end='')

    return characters_src, characters_dest

if __name__ == '__main__':
    import doctest
    doctest.testmod()
