maximum = 1000
numbers = set(range(1, maximum + 1))
divisible_by_3 = {number for number in numbers if not number % 3}
divisible_by_7 = {number for number in numbers if not number % 7}
divisible_by_11 = {number for number in numbers if not number % 11}

A = divisible_by_3 & divisible_by_7 & divisible_by_11
B = (divisible_by_3 & divisible_by_7) - divisible_by_11
C = numbers - divisible_by_3 - divisible_by_7 - divisible_by_11
