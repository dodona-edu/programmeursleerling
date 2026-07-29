class SubsetChecker(OutputProcessor):

    """
    Checks whether the return value is a non-empty sub-collection of the given
    list of numbers that adds up to zero. Such a subset is not necessarily
    unique, so the return value cannot simply be compared to the one produced
    by the sample solution.
    """

    def checkReturnValue(self, expected, generated, **kwargs):

        numbers = list(self.getParameter('numbers'))

        def setMessage(message):

            self.addMessage('Error: ' + message)
            self.setGeneratedOutput(
                channel='return',
                output=generated
            )

        # the subset must be a list of numbers
        if not isinstance(generated, list):
            setMessage('the subset must be a list')
            return False

        # the empty subset adds up to zero, but does not solve the problem
        if not generated:
            setMessage('the subset must contain at least one number')
            return False

        # every number of the subset must be taken from the given list, and no
        # number can be taken more often than it occurs in the given list
        remaining = list(numbers)
        for number in generated:
            if number not in remaining:
                setMessage('the subset contains numbers that are not in the given list')
                return False
            remaining.remove(number)

        # the numbers of the subset must add up to zero
        if sum(generated) != 0:
            setMessage('the numbers of the subset do not add up to zero')
            return False

        # generated return value passed all tests
        return True
