# read number of pirates
pirates = int(input())

# determine minimal number of coconuts
coconuts = 0
while True:
    coconuts += 1
    pile = coconuts
    for i in range( pirates ):
        if pile % pirates != 1:
            break
        pile = (pirates-1) * int( (pile - 1) / pirates )
    if pile % pirates == 1:
        break

# print minimal number of coconuts
print( coconuts )
