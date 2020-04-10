def hanoi(grootte):

    """
    >>> hanoi(4)
    Schijf 1 van A naar B
    Schijf 2 van A naar C
    Schijf 1 van B naar C
    Schijf 3 van A naar B
    Schijf 1 van C naar A
    Schijf 2 van C naar B
    Schijf 1 van A naar B
    Schijf 4 van A naar C
    Schijf 1 van B naar C
    Schijf 2 van B naar A
    Schijf 1 van C naar A
    Schijf 3 van B naar C
    Schijf 1 van A naar B
    Schijf 2 van A naar C
    Schijf 1 van B naar C
    15 stappen gedaan
    """

    stappen = hanoi_recursie('A', 'B', 'C', grootte)
    print(stappen, "stappen gedaan")

def hanoi_recursie( p_van, p_tmp, p_naar, grootte ):
    if grootte == 1:
        print( "Schijf 1 van", p_van, "naar", p_naar )
        return 1
    stappen = hanoi_recursie( p_van, p_naar, p_tmp, grootte-1 )
    print( "Schijf", grootte, "van", p_van, "naar", p_naar )
    stappen += 1 + hanoi_recursie( p_tmp, p_van, p_naar, grootte-1 )
    return stappen

if __name__ == '__main__':
    import doctest
    doctest.testmod()