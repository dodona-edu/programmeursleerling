import os
import random

def create_dir(*path):

    # compose path
    path = os.path.join(*path)

    # create dir if it doesn't already exist
    if not os.path.exists(path):
        os.makedirs(path)

    # return path
    return path

def arguments_str(*args, **kwargs):

    args_str = ''

    # add positional arguments
    for value in args:
        if args_str:
            args_str += ', '
        args_str += repr(value)

    # add keyword arguments
    kwargs = list(kwargs.items())
    random.shuffle(kwargs)
    for name, value in kwargs:
        if args_str:
            args_str += ', '
        args_str += f'{name}={value!r}'

    return args_str

def test_instantiation(_class, *args, varname=None, newcontext=True, **kwargs):

    variable = f'{varname} = ' if varname is not None else ''
    context = ' # doctest: +NEWCONTEXT' if newcontext else ''
    if varname is None:
        context += ' +REPR'

    # generate test statement
    print(f'>>> {variable}{_class.__name__}({arguments_str(*args, **kwargs)}){context}')

    # instantiate object
    obj = _class(*args, **kwargs)

    # generate test result
    if varname is None:
        print(f'{obj!r}')

    # return instantiated object
    return obj

def test_repr(obj, varname=None, call=None):

    if call is None:
        call = random.choice((True, False))

    if varname is None:
        varname = repr(obj)

    if call:

        # generate test statement
        print(f'>>> repr({varname})')

        # generate test result
        print(f'{repr(obj)!r}')

    else:

        # generate test statement
        print(f'>>> {varname} # doctest: +REPR')

        # generate test result
        print(f'{obj!r}')

def test_str(obj, varname=None, call=None):

    if call is None:
        call = random.choice((True, False))

    if varname is None:
        varname = repr(obj)

    if call:

        # generate test statement
        print(f'>>> str({varname})')

        # generate test result
        print(f'{str(obj)!r}')

    else:

        # generate test statement
        print(f'>>> print({varname}) # doctest: +STDOUT')

        # generate test result
        print(obj)

def test_property(obj, property, varname=None):

    if varname is None:
        varname = repr(obj)

    # generate test statement
    print(f'>>> {varname}.{property}')

    # generate test result
    print(repr(getattr(obj, property)))

def test_method(obj, method, *args, varname=None, processor=None, **kwargs):

    if varname is None:
        varname = repr(obj)

    # generate test statement
    method = getattr(obj.__class__, method)
    print(f'>>> {varname}.{method.__name__}({arguments_str(*args, **kwargs)})')

    try:

        # compute test result
        result = method(obj, *args, **kwargs)

        if processor is not None:
            print(processor.rstrip())

        # generate test result
        if result is not None:
            print(f'{result!r}')

        # return test result
        return result

    except Exception as e:

        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))
