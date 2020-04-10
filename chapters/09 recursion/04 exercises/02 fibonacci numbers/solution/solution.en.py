def fib(number, depth):

    """
    >>> fib(5, 0)
    fib(5, 0)
      fib(4, 1)
        fib(3, 2)
          fib(2, 3)
            fib(1, 4)
            return 1
            fib(0, 4)
            return 0
          return 1
          fib(1, 3)
          return 1
        return 2
        fib(2, 2)
          fib(1, 3)
          return 1
          fib(0, 3)
          return 0
        return 1
      return 3
      fib(3, 1)
        fib(2, 2)
          fib(1, 3)
          return 1
          fib(0, 3)
          return 0
        return 1
        fib(1, 2)
        return 1
      return 2
    return 5
    5
    """

    indentation = '  ' * depth
    print(f'{indentation}fib({number}, {depth})')

    resultaat = (
        fib(number - 1, depth + 1) + fib(number - 2, depth + 1)
        if number > 1 else number
    )

    print(f'{indentation}return {resultaat}')
    return resultaat

if __name__ == '__main__':
    import doctest
    doctest.testmod()
