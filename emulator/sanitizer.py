def get_instructions(path):
    """Reads the instruction sequence from the path."""
    instructions = None

    try:
        with open(path) as f:
            seq = f.read()

        invalid_instructions = _identify_invalid_instructions(seq)

        if len(invalid_instructions) > 0:
            _display_invalid_instructions(invalid_isntructions)
        else:
            instructions = _linearify(seq)
    except IOError:
        print("Cannot open {}".format(path))
        print("Check that the file exists.")

    return instructions


def _linearify(seq):
    """Format sequence into an array of instructions."""
    seq = seq.replace('\n', ' ').replace('\r', ' ').split(' ')
    seq = filter(lambda x: len(x) > 0, seq)

    return list(seq)


def _instruction_in_range(instruction):
    return 0 <= instruction <= 15


def _identify_invalid_instructions(seq):
    """Identifies invalid instructions."""
    invalid = []
    seq = seq.split('\n')

    for i in range(len(seq)):
        line = i + 1

        for code in list(filter(lambda x: len(x) > 0, seq[i].split(' '))):
            try:
                code = int(code)

                if not _instruction_in_range(code):
                    invalid.append({
                        'code'  : code,
                        'line'  : line,
                        'error' : SyntaxError
                    })
            except ValueError:
                invalid.append({
                    'code'  : code,
                    'line'  : line,
                    'error' : ValueError
                })

    return invalid


def _display_invalid_instructions(seq):
    """Displays the invalid instructions."""
    for invalid in seq:
        if invalid['error'] == SyntaxError:
            message = 'SyntaxError: unknown instruction code'
        elif invalid['error'] == ValueError:
            message = 'ValueError: non integer instruction'
        else:
            message = 'Invalid instruction code'

        print('Line {}, instruction \'{}\' -> {}'.format(invalid['line'],
            invalid['code'], message))
