def push(queue, element):

    """
    >>> queue = ['appel', 'peer']
    >>> push(queue, 'vijg')
    >>> queue
    ['appel', 'peer', 'vijg']
    """

    queue.append(element)

def pop(queue):

    """
    >>> queue = ['appel', 'peer']
    >>> pop(queue)
    'appel'
    >>> queue
    ['peer']
    >>> pop(queue)
    'peer'
    >>> pop(queue)
    """

    if not queue:
        return None

    return queue.pop(0)

def verwerk(regels):

    """
    >>> verwerk(['appel', 'peer', '?', '?', '?', '', 'vijg'])
    appel
    peer
    De queue is leeg.
    """

    queue = []
    for regel in regels:

        if regel == '':
            # de gebruiker drukte alleen op de Enter toets, dus het programma
            # eindigt
            break

        if regel == '?':
            # de gebruiker vraagt het eerste element van de queue op
            element = pop(queue)
            if element is None:
                print('De queue is leeg.')
            else:
                print(element)
        else:
            # de gebruiker voert een nieuw element voor de queue in
            push(queue, regel)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
