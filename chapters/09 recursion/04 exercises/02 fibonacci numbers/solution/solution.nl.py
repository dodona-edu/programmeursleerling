def fib(getal, diepte):

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

    insprong = '  ' * diepte
    print(f'{insprong}fib({getal}, {diepte})')

    resultaat = (
        fib(getal - 1, diepte + 1) + fib(getal - 2, diepte + 1)
        if getal > 1 else getal
    )

    print(f'{insprong}return {resultaat}')
    return resultaat

if __name__ == '__main__':
    import doctest
    doctest.testmod()
