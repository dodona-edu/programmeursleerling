def vraag_input( prompt ):
    waarde = input( prompt )
    if not waarde.islower():
        print("Ongeldig antwoord!")
        waarde = vraag_input( prompt ) # DOE DIT NIET!
    return waarde

s = vraag_input( "Geef een string van kleine letters: " )
print( "Je gaf in:", s )
