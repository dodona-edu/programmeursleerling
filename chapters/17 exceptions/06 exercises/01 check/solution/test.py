def customEvaluate(expected_output, generated_output):

    # check if there's  a single line of output
    if len(generated_output) != 1:
        return False

    # extract output lines
    expected_output = expected_output[0]
    generated_output = generated_output[0]

    # expected error message > check if also generated error message
    for prefix in ('Error', 'Fout'):
        prefix = f'{prefix}: '
        if expected_output.startswith(prefix):
            return generated_output.startswith(prefix)

    # check formatting of regular generated output
    import re
    exp = re.match('(-?[0-9]+ / -?[0-9]+) = ([0-9]*.[0-9]+|[0-9]+.[0-9]*)$', expected_output)
    gen = re.match('(-?[0-9]+ / -?[0-9]+) = ([0-9]*.[0-9]+|[0-9]+.[0-9]*)$', generated_output)
    if not exp or not gen:
        return False

    # check prefix and suffix of regular generated output
    return (
        gen[1] == exp[1] and                         # same prefix
        abs(float(gen[2]) - float(exp[2])) < 1e-6    # same suffix (float)
    )

expected = ['100 / 100 = 1.0']
generated = ['100 / 100 = 1.0']
print(customEvaluate(expected, generated))