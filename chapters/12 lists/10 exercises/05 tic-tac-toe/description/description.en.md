Write a Tic-Tac-Toe program that allows two
people to play the game against each other. In turn, ask each player
which row and column they want to play. Make sure that the program
checks if that row/column combination is empty. When a player has won,
end the game. When the whole board is full and there is no winner,
announce a draw.

This is a fairly long program to write (60 lines or so). It will
definitely help to use some functions. I recommend that you create a
function `display\_board()` that gets the board as parameter and
displays it, a function `getRowCol()` that asks for a row or a column
(depending on a parameter) and checks whether the user entered a legal
value, and a function `winner()` that gets the board as argument and
checks if there is a winner. Keep track of who the current player is
using a global variable `player` that you can pass to a function as an
argument if the function needs it. I also use a function `opponent()`,
that takes the player as argument and returns the opponent. I use that
to switch players after each move.

The main program will be something along the lines of (in pseudo-code):

    display board
    while True:
        ask for row
        ask for column
        if row/column combination already occupied:
            display error message
            continue
        place player marker on row/column combination
        display board
        if there is a winner:
            announce winner
            break
        if the board is full:
            announce draw
            break
        switch players

### Assignment

Represent the board as a list (`list`) of three rows, where each row is a list (`list`) of three strings (`str`): `X` for a cell taken by the first player, `O` for a cell taken by the second player, and `.` for an empty cell. Rows and columns are numbered 1 up to and including 3. Write the following five functions, and use them to write the main program sketched above.

- Write a function `opponent` that takes a player (`X` or `O`). The function must return the other player.

- Write a function `display_board` that takes a board. The function must print the board, preceded by a line that holds the column numbers, and with every row preceded by its row number. Separate the cells of a row by a single space.

- Write a function `place` that takes a board, a player, a row and a column. If the given row and column are on the board and the corresponding cell is still empty, then the function must place the marker of the given player in that cell and return `True`. Otherwise, the function must leave the board untouched and return `False`.

- Write a function `winner` that takes a board. If a player has three markers on a row, on a column or on a diagonal, then the function must return that player. Otherwise, the function must return `None`.

- Write a function `full` that takes a board. The function must return a Boolean value (`bool`) that indicates whether all cells of the board are taken.

### Example

```console?lang=python&prompt=>>>
>>> opponent('X')
'O'
>>> board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
>>> place(board, 'X', 2, 2)
True
>>> place(board, 'O', 2, 2)
False
>>> place(board, 'O', 4, 1)
False
>>> place(board, 'O', 1, 3)
True
>>> display_board(board)
  1 2 3
1 . . O
2 . X .
3 . . .
>>> winner(board)
>>> full(board)
False
>>> display_board([['X', 'O', 'O'], ['.', 'X', '.'], ['O', '.', 'X']])
  1 2 3
1 X O O
2 . X .
3 O . X
>>> winner([['X', 'O', 'O'], ['.', 'X', '.'], ['O', '.', 'X']])
'X'
>>> full([['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']])
True
```
