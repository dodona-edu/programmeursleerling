class GridChecker(OutputProcessor):

    """
    Checks whether the return value is a grid that holds three randomly placed
    battleships that do not touch each other horizontally or vertically. Such a
    grid is not unique, so the return value cannot simply be compared to the one
    produced by the sample solution.
    """

    def checkReturnValue(self, expected, generated, **kwargs):

        # keep track of the generated grids
        repeats = 20
        grids = set()

        def setMessage(message):

            self.addMessage('Error: ' + message)
            self.setGeneratedOutput(
                channel='return',
                output=generated
            )

        def is_valid_grid(grid):

            # the grid must have three rows of four cells, and each cell must
            # either be empty or hold a battleship
            if (
                not isinstance(grid, list) or
                len(grid) != 3 or
                not all(isinstance(row, list) and len(row) == 4 for row in grid)
            ):
                setMessage('the grid must have three rows of four cells')
                return False

            if not all(cell in ('.', 'X') for row in grid for cell in row):
                setMessage('the cells of the grid must be either . or X')
                return False

            # the grid must hide exactly three battleships
            cells = [
                (row, column)
                for row in range(3) for column in range(4)
                if grid[row][column] == 'X'
            ]
            if len(cells) != 3:
                setMessage(
                    'the grid must hide three battleships but hides {}'.format(len(cells))
                )
                return False

            # battleships are not allowed to touch each other horizontally or
            # vertically
            for row1, column1 in cells:
                for row2, column2 in cells:
                    if abs(row1 - row2) + abs(column1 - column2) == 1:
                        setMessage('battleships are not allowed to touch each other')
                        return False

            grids.add(tuple(tuple(row) for row in grid))

            return True

        # check initial return value
        if not is_valid_grid(generated):
            return False

        # repetitively check if the function returns a valid grid
        for _ in range(repeats - 1):

            # re-evaluate expression
            try:
                generated = self.executeStatement(
                    channels=['return'],
                    expected_type=[[str]]
                )
            except:
                return False

            # check new return value
            if not is_valid_grid(generated):
                return False

        # check if the battleships are placed randomly
        if len(grids) < repeats // 2:
            setMessage('battleships are not placed randomly')
            return False

        # generated return value passed all tests
        return True
