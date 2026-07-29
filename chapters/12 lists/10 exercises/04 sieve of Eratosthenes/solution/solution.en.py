def sieve(n):

    """
    >>> sieve(10)
    [2, 3, 5, 7]
    >>> sieve(1)
    []
    """

    # start from the sequence of numbers from 0 up to and including n
    numbers = list(range(max(n + 1, 0)))

    # neither 0 nor 1 is prime
    for index in range(min(2, len(numbers))):
        numbers[index] = 0

    # zero out all multiples of every number that is still on the list
    for number in range(2, len(numbers)):
        if numbers[number] != 0:
            for multiple in range(2 * number, len(numbers), number):
                numbers[multiple] = 0

    # the numbers that are left on the list are the primes
    return [number for number in numbers if number != 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
