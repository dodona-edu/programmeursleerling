The elements of a list may be lists themselves (which also may contains
lists, etcetera). This is a good way to create a matrix in a program.
For instance, you can create a Tic-Tac-Toe board, where a dash (-)
represents an empty cell, as follows:

```python
board = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]
```

The first row of the board is represented by `board[0]`, the second row
by `board[1]`, and the third row by `board[2]`. If you want to access
the first cell of the first row, that is `board[0][0]`, the second cell
is `board[0][1]` and the third cell is `board[0][2]`. For example, the
following code places an "X" in the middle of the board, and an "O" in
the upper right corner. It also displays the board in a nice way (with
markers for rows and columns around it).

```python
def display_board( b ):
    print( "  1 2 3" )
    for row in range( 3 ):
        print( row+1, end=" ")
        for col in range( 3 ):
            print( b[row][col], end=" " )
        print()

board = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]
board[1][1] = "X"
board[0][2] = "O"
display_board( board )
```
