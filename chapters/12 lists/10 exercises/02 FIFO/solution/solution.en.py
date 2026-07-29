def push(queue, element):

    """
    >>> queue = ['apple', 'pear']
    >>> push(queue, 'fig')
    >>> queue
    ['apple', 'pear', 'fig']
    """

    queue.append(element)

def pop(queue):

    """
    >>> queue = ['apple', 'pear']
    >>> pop(queue)
    'apple'
    >>> queue
    ['pear']
    >>> pop(queue)
    'pear'
    >>> pop(queue)
    """

    if not queue:
        return None

    return queue.pop(0)

def process(lines):

    """
    >>> process(['apple', 'pear', '?', '?', '?', '', 'fig'])
    apple
    pear
    The queue is empty.
    """

    queue = []
    for line in lines:

        if line == '':
            # the user just pressed the Enter key, so the program ends
            break

        if line == '?':
            # the user wants the first element of the queue
            element = pop(queue)
            if element is None:
                print('The queue is empty.')
            else:
                print(element)
        else:
            # the user entered a new element for the queue
            push(queue, line)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
