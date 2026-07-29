import random

# pick the number that has to be guessed
number = random.randint(1, 1000)

# read guesses until the number has been guessed
attempts = 0
guessed = False
while not guessed:

    # read the next guess
    guess = int(input())
    attempts += 1

    # tell how the number to guess relates to the guess
    if number < guess:
        print('Lower')
    elif number > guess:
        print('Higher')
    else:
        print('You guessed it!')
        guessed = True

# report the number of attempts that were needed
print(f'Number of attempts: {attempts}')
