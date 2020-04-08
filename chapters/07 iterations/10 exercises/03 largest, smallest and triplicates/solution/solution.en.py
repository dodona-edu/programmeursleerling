# read first number
number = int(input())

# initialise statistics
largest = number
smallest = number
triplicates = 0 if number % 3 else 1

# read and process remaining numbers
for _ in range(9):

    # read next number
    number = int(input())

    # update largest
    if number > largest:
        largest = number

    # update smallest
    if number < smallest:
        smallest = number

    # update triplicates
    if not number % 3:
        triplicates += 1

# print statistics
print(f'largest: {largest}')
print(f'smallest: {smallest}')
print(f'triplicates: {triplicates}')
