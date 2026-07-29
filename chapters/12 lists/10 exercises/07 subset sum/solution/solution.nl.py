def subset_som(getallen):

    """
    >>> subset_som([1, 4, -3, -5, 7])
    [1, 4, -5]
    >>> subset_som([1, 4, -3, 7])
    """

    def zoek(index, gekozen, som):

        # een niet-lege deelverzameling die optelt tot nul lost het probleem op
        if gekozen and som == 0:
            return gekozen

        # alle getallen werden bekeken zonder een oplossing te vinden
        if index == len(getallen):
            return None

        # probeer het probleem eerst op te lossen met het huidige getal erbij
        oplossing = zoek(
            index + 1, gekozen + [getallen[index]], som + getallen[index]
        )
        if oplossing is not None:
            return oplossing

        # probeer het anders op te lossen zonder het huidige getal
        return zoek(index + 1, gekozen, som)

    return zoek(0, [], 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
