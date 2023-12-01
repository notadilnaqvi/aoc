def read_from_file(file):
    data = None
    with open(file) as f:
        data = f.read()
    return data


def extract_type_and_value(signal):
    signal = dict(enumerate(signal.split(' ')))
    instruction_type = signal.get(0)
    signal_value = signal.get(1, None)
    return [instruction_type, signal_value]


def solve(file):
    input_value = read_from_file(file)
    signals = input_value.splitlines()

    x_register_value = 1
    cycles = []
    for signal in signals:
        [instruction_type, signal_value] = extract_type_and_value(signal)

        if instruction_type == 'noop':
            cycles.append(x_register_value)
        elif instruction_type == 'addx':
            cycles.append(x_register_value)
            cycles.append(x_register_value)
            x_register_value += int(signal_value)

    pixels = ''
    print(cycles)
    cycles = dict(enumerate(cycles))
    for col in range(0, 40):
        for row in range(0, 6):
            if col + 1 in [cycles.get(row - 1, None), cycles.get(row, None), cycles.get(row + 1, None)]:
                pixels += '#'
            else:
                pixels += '.'
    
    print(pixels)

solve('sample.txt')
# solve('input.txt')
