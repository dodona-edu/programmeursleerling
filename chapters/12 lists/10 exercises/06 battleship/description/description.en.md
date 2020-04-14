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
