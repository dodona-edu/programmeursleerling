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
