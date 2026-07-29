Create a program that is a simplified
version of the game "Battleship." The computer creates (in memory) a
grid that is 4 cells wide and 3 cells high. The rows of the grid are
numbered 1 to 3, and the columns of the grid are labeled A to D. The
computer hides a battleship in three random cells in the grid. Each
battleship occupies exactly one cell. Battleships are not allowed to
touch each other horizontally or vertically. Make sure that the program
places the battleships randomly, so not pre-configured.

The computer asks the player to "shoot" at cells of the grid. The player
does so by entering the column letter and row number of the cell which
he wants to shoot at (e.g., `"D3"`). If the cell which the player shoots
at contains nothing, the computer responds with "Miss!" If the cell
contains a battleship, the computer responds with "You sunk my
battleship!" and removes the battleship from the cell (i.e., a second
shot at the same cell is a miss). As soon as the player hits the last
battleship, the computer responds with displaying how many shots the
player needed to shoot down all three battleships, and the program ends.

To help with debugging the game, at the start the computer should
display the grid with periods marking empty cells and `X`s marking cells
with battleships.

Hint: If you have troubles with this exercise, start by using a board
which has the battleships already placed. Once the rest of the code
works, add a function that places the battleships at random, at first
without checking if they are touching one another. Once that works, add
code that disallows battleships touching each other.

### Assignment

Represent the grid as a list (`list`) of three rows, where each row is a list (`list`) of four strings (`str`): `X` for a cell that hides a battleship, and `.` for an empty cell. A cell of the grid is referred to by a string (`str`) that holds its column letter (`A` up to and including `D`) followed by its row number (`1` up to and including `3`). Write the following four functions, and use them to write the game.

- Write a function `place_ships` that takes no arguments. The function must return a new grid that hides three battleships in three randomly chosen cells. Battleships are not allowed to touch each other horizontally or vertically.

- Write a function `display_grid` that takes a grid. The function must print the grid, preceded by a line that holds the column letters, and with every row preceded by its row number. Separate the cells of a row by a single space.

- Write a function `ships` that takes a grid. The function must return how many battleships the grid still hides.

- Write a function `shoot` that takes a grid and a cell. If the given cell hides a battleship, then the function must remove that battleship from the grid and return the string `You sunk my battleship!`. Otherwise, the function must return the string `Miss!`. If the given cell is not on the grid, then the function must raise an `AssertionError` with the message `invalid cell`.

### Example

```console?lang=python&prompt=>>>
>>> grid = [['.', '.', 'X', '.'], ['X', '.', '.', '.'], ['.', '.', 'X', '.']]
>>> display_grid(grid)
  A B C D
1 . . X .
2 X . . .
3 . . X .
>>> ships(grid)
3
>>> shoot(grid, 'C1')
'You sunk my battleship!'
>>> shoot(grid, 'C1')
'Miss!'
>>> shoot(grid, 'B2')
'Miss!'
>>> ships(grid)
2
>>> shoot(grid, 'E1')
Traceback (most recent call last):
AssertionError: invalid cell
>>> ships(place_ships())
3
```
