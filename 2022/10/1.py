def read_from_file(file):
    data = None
    with open(file) as f:
        data = f.read()
    return data

instruction_TYPE_TO_CYCLE_NUMBER_MAPPING = {
    'noop': 1,
    'addx': 2,
}


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

        # print(instruction_type, signal_value, '-->', x_register_value)


    solution = 0
    for index,cycle in enumerate(cycles):

        if(index + 1 == 20 or index + 1 == 60 or index + 1 == 100 or index + 1 == 140 or index + 1 == 180 or index + 1 == 220):
            solution += (index+1) * cycle

    print(cycles)



# solve('sample.txt')
solve('input.txt')
