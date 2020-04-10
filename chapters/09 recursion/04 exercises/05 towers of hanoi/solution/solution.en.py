def hanoi(size):

    """
    >>> hanoi(4)
    Disc 1 from A to B
    Disc 2 from A to C
    Disc 1 from B to C
    Disc 3 from A to B
    Disc 1 from C to A
    Disc 2 from C to B
    Disc 1 from A to B
    Disc 4 from A to C
    Disc 1 from B to C
    Disc 2 from B to A
    Disc 1 from C to A
    Disc 3 from B to C
    Disc 1 from A to B
    Disc 2 from A to C
    Disc 1 from B to C
    15 moves needed
    """

    moves = solve_hanoi('A', 'B', 'C', size)
    print(moves, "moves needed")

def solve_hanoi( pole_from, pole_tmp, pole_to, size ):
    if size == 1:
        print( "Disc 1 from", pole_from, "to", pole_to )
        return 1
    moves = solve_hanoi( pole_from, pole_to, pole_tmp, size-1 )
    print( "Disc", size, "from", pole_from, "to", pole_to )
    moves += 1+solve_hanoi( pole_tmp, pole_from, pole_to, size-1)
    return moves

if __name__ == '__main__':
    import doctest
    doctest.testmod()