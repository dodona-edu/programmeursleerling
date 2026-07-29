def subset_sum(numbers):

    """
    >>> subset_sum([1, 4, -3, -5, 7])
    [1, 4, -5]
    >>> subset_sum([1, 4, -3, 7])
    """

    def search(index, selected, total):

        # a non-empty selection that adds up to zero solves the problem
        if selected and total == 0:
            return selected

        # all numbers have been considered without finding a solution
        if index == len(numbers):
            return None

        # first try to solve the problem with the current number selected
        solution = search(
            index + 1, selected + [numbers[index]], total + numbers[index]
        )
        if solution is not None:
            return solution

        # otherwise try to solve the problem without the current number
        return search(index + 1, selected, total)

    return search(0, [], 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
