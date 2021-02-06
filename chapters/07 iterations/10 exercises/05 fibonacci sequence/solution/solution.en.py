# read upper limit
upper_limit = int(input())

# print Fibonacci sequence
previous, next = 0, 1
print(previous)
while previous <= upper_limit:
    print(next)
    previous, next = next, previous + next
