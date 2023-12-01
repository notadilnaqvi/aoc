def read_from_file(file):
    data = None
    with open(file) as f:
        data = f.read()
    return data

CHARACTERS_IN_START_OF_MESSAGE_MARKER = 14

def check_for_duplicates(sequence):
    # If after removing (possible) duplicates, the length of the sequence changes,
    # then that would mean that there were duplicates (that got removed).
    return len(set(sequence)) != CHARACTERS_IN_START_OF_MESSAGE_MARKER

def solve(file):
    datastream = read_from_file(file)
    for index, _ in enumerate(datastream):
        has_duplicates = check_for_duplicates(datastream[index:index + CHARACTERS_IN_START_OF_MESSAGE_MARKER])
        if not has_duplicates:
            print(f'[{file}]: {index + CHARACTERS_IN_START_OF_MESSAGE_MARKER}')
            break


solve('sample-1.txt')
solve('sample-2.txt')
solve('sample-3.txt')
solve('sample-4.txt')
solve('input.txt')
