from random import randint

NUMCRAWLERS = 1000000000
num = NUMCRAWLERS
die = int( num / 3 )
if NUMCRAWLERS % 3:
    if randint( 0, NUMCRAWLERS % 3 ): # Remaining on day 1
        die += 1
totalage = die # Day-1 deaths added to totalage
num -= die

age = 2
while num > 0:
    die = int( num / 2 )
    num -= die # Kill off half the population
    if die != num: # There is a single remaining
        if randint( 0, 1 ): # Decide on kill of single
            die, num = num, die # swap values
    totalage += die * age
    age += 1

print( "{:.2f}".format( totalage / NUMCRAWLERS ) )
