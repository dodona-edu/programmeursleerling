# read upper limit
upper_limit = int(input())

# print Fibonacci sequence
previous, next = 0, 1
while previous <= upper_limit:
    print(previous)
    previous, next = next, previous + next

# print first number that exceeds upper limit
print(next)
