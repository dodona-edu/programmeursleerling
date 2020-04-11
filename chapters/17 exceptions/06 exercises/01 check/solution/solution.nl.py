numlist = [ 100, 101, 0, "103", 104 ]

try:
    i1 = int( input( "Geef een index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except ValueError:
    print( "Fout: je gaf geen geheel getal" )
except IndexError:
    print( "Fout: de index moet tussen -5 en 4 liggen" )
except ZeroDivisionError:
    print( "Fout: het lijkt erop dat de list een 0 bevat" )
except TypeError:
    print( "Fout: het lijkt erop er een niet-numeriek element is" )
except:
    print( "Fout: er is iets onverwachts gebeurd" )
    raise
