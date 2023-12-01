def read_from_file(file):
    data = None
    with open(file) as f:
        data = f.read()
    return data

def solve(file):
    datastream = read_from_file(file)


solve('sample.txt')
solve('input.txt')
