# read integer
number = int(input())

# determine if number is a prime
prime = True
divisor = 2
while prime and divisor < number:
    if not number % divisor:
        prime = False
    divisor += 1

# print result
print(f'{number} is{"" if prime else " not"} a prime')
