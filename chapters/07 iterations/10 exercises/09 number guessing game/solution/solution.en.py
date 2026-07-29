# the number to guess still lies between these two numbers
smallest = 1
largest = 1000

# guess as long as a number is possible and the number has not been guessed
attempts = 0
guessed = False
while not guessed and smallest <= largest:

    # guess the middle of the numbers that are still possible
    guess = (smallest + largest) // 2
    attempts += 1
    print(f'Is it {guess}?')

    # process the answer of the user
    answer = input()
    if answer == 'C':
        guessed = True
    elif answer == 'L':
        largest = guess - 1
    else:
        smallest = guess + 1

# report the number of attempts, or that the answers were impossible
if guessed:
    print(f'Number of attempts: {attempts}')
else:
    print('That is impossible!')
