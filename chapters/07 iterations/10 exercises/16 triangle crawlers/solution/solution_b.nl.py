schatting = 1/3
rest = 2/3
for dagen in range( 2, 101 ):
    rest /= 2
    schatting += rest * dagen
print( "{:.2f}".format( schatting ) )
