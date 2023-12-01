def read_from_file(file):
    data = None
    with open(file) as f:
        data = f.read()
    return data