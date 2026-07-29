from collections import Counter
from statistics import mean, median

def mode(numbers):

    """
    >>> mode([1, 2, 2, 3])
    [2]
    """

    if not numbers:
        return []

    counts = Counter(numbers)
    highest = counts.most_common(1)[0][1]
    if highest < 2:
        return []

    return sorted(number for number, count in counts.items() if count == highest)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    numbers = []
    while True:
        number = int(input('Enter a number (0 to stop): '))
        if number == 0:
            break
        numbers.append(number)

    print('mean:', mean(numbers))
    print('median:', median(numbers))
    modes = mode(numbers)
    if modes:
        print('mode:', ', '.join(str(number) for number in modes))
    else:
        print('there is no mode')
