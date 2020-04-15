"""
>>> print(open('data.txt', 'r').read(), end='')
How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood.
>>> zonder_klinkers('data.txt', 'kopie.txt')
(190, 135)
>>> print(open('kopie.txt', 'r').read(), end='')
Hw mch wd wld  wdchck chck
f  wdchck cld chck wd?
H wld chck, h wld, s mch s h cld,
nd chck s mch s  wdchck wld
f  wdchck cld chck wd.
"""

def zonder_klinkers(bronbestand, doelbestand):

    karakters_invoer = 0
    karakters_uitvoer = 0

    with open(bronbestand, 'r') as bron:
        with open(doelbestand, 'w') as doel:
            for regel in bron:
                karakters_invoer += len(regel)
                regel = ''.join(
                    karakter for karakter in regel
                    if karakter.lower() not in 'aeiou'
                )
                karakters_uitvoer += len(regel)
                print(regel, file=doel, end='')

    return karakters_invoer, karakters_uitvoer

if __name__ == '__main__':
    import doctest
    doctest.testmod()
