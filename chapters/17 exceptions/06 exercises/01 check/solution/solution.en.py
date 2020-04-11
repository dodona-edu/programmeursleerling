numlist = [ 100, 101, 0, "103", 104 ]

try:
    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except ValueError:
    print( "Error: you did not enter an integer" )
except IndexError:
    print( "Error: you should specify an index between -5 and 4" )
except ZeroDivisionError:
    print( "Error: it looks like the list contains a zero" )
except TypeError:
    print( "Error: it looks like there is a non-numeric item" )
except:
    print( "Error: something unexpected happened" )
    raise
