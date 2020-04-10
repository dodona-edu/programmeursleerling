def get_input( prompt ):
    value = input( prompt )
    if not value.islower():
        print( "Invalid answer!")
        value = get_input( prompt ) # DO NOT DO THIS!
    return value

s = get_input( "Give a string of lower case letters: " )
print( "The user entered:", s )
