class DeckChecker(OutputProcessor):

    """
    Checks whether the return value is a random shuffle of a standard card deck.
    """

    def checkReturnValue(self, expected, generated, **kwargs):

        # keep track of generated decks
        repeats = 20
        decks = set()
        expected = set(expected)

        def setMessage(message):

            self.addMessage('Error: ' + message)

        def listing(container):

            if len(container) == 0:
                return ''

            if len(container) < 6:
                return ', '.join(container)

            return ', '.join(container[:5]) + f', ... ({len(container) - 5} more)'

        def is_valid_deck(deck):

            valid = False
            if len(deck) != len(set(deck)):
                invalid = sorted({card for card in deck if deck.count(card) > 1})
                message = f'deck contains duplicate cards: {listing(invalid)}'
            elif not set(deck) <= expected:
                invalid = sorted(set(deck) - expected)
                message = f'deck contains invalid cards: {listing(invalid)}'
            elif len(deck) != len(expected):
                message = f'deck should contain {len(expected)} cards but contains {len(deck)} cards'
            else:
                valid = True

            if not valid:
                setMessage(message)
                self.setGeneratedOutput(
                    channel='return',
                    output=deck
                )
            else:
                decks.add(tuple(deck))

            return valid

        # check initial return value
        if not is_valid_deck(generated):
            return False

        # repetively check if function returns a randomly shuffled deck
        for _ in range(repeats - 1):

            # re-evaluate expression
            try:
                generated = self.executeStatement(
                    channels=['return'],
                    expected_type=[str]
                )
            except:
                return False

            # check new return value
            if not is_valid_deck(generated):
                return False

        # check if decks are randomly shuffled
        if len(decks) < repeats // 2:
            setMessage('generated decks are not randomly shuffled')
            return False

        # generated return value passed all tests
        return True
