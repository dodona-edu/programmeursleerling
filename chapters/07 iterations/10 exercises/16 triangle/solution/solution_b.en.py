estimate = 1/3
remainder = 2/3
for days in range( 2, 101 ):
    remainder /= 2
    estimate += remainder * days
print( "{:.2f}".format( estimate ) )
