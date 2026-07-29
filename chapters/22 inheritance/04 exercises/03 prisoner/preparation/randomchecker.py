class RandomMoveChecker(OutputProcessor):

    """
    Checks whether the method returns a move that was picked at random. A
    strategy that plays at random may call the random module in any reasonable
    way, so the sequence of moves it returns is not unique and cannot simply be
    compared to the one produced by the sample solution. Instead of pinning
    down one exact sequence, the shape of the returned moves is checked: the
    method is called 100 times, every call must return a valid move ('C' or
    'D'), and each of the two moves must be returned at least 10 times. A
    strategy that really picks its move at random passes this test unless it is
    extremely unlucky (the odds of getting fewer than 10 of either move out of
    100 calls are about 1 in 10^17), whereas a strategy that keeps returning
    the same move is always caught.
    """

    def checkReturnValue(self, expected, generated, **kwargs):

        # number of times the method is called, and the minimal number of times
        # each of the two moves must be returned across those calls
        repeats = 100
        threshold = 10

        # keep track of how often each move was returned
        moves = ('C', 'D')
        counts = {move: 0 for move in moves}

        def setMessage(message):

            self.addMessage('Error: ' + message)
            self.setGeneratedOutput(
                channel='return',
                output=generated
            )

        def is_valid_move(move):

            if move not in moves:
                setMessage(
                    "the method must return either 'C' or 'D', but returned {!r}".format(move)
                )
                return False

            counts[move] += 1

            return True

        # check initial return value
        if not is_valid_move(generated):
            return False

        # repetitively check if the method returns a valid move
        for _ in range(repeats - 1):

            # re-evaluate expression
            try:
                generated = self.executeStatement(
                    channels=['return'],
                    expected_type=str
                )
            except:
                return False

            # check new return value
            if not is_valid_move(generated):
                return False

        # check if the moves are picked at random
        for move in moves:
            if counts[move] < threshold:
                setMessage(
                    'the method returned {!r} only {} out of {} times, so the '
                    'move is not picked at random'.format(
                        move, counts[move], repeats
                    )
                )
                return False

        # generated return value passed all tests
        return True
