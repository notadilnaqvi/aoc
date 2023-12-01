import re
from pprint import pp

def read_from_file(file):
    data = None
    with open(file) as f:
        data = f.read()
    return data

CHANGE_DIR_COMMAND_REGEX = '\$\scd\s'

def solve(file):
    input_value = read_from_file(file)
    chunks = re.split(CHANGE_DIR_COMMAND_REGEX, input_value)
    dirs = {}
    for chunk in chunks:
        commands = chunk.split('\n')
        if commands[0] == '' or commands[0] == '..':
            continue
        dirs[commands[0]] = {"dirs": [], "files_sizes": []}
        for index, command in enumerate(commands):
            if command.startswith('$') or index == 0 or not command:
                continue
            if command.startswith('dir'):
                print('dir: ', command.split(' ')[1])
                dirs[commands[0]]['dirs'].append(command.split(' ')[1])
            else:
                print('file_size: ', command.split(' ')[0])
                dirs[commands[0]]['files_sizes'].append(command.split(' ')[0])

    for d in dirs:

    


def calc_file_size(d):
    if d['files_sizes']:
        for file_size in d['files_sizes']:
            total_file_size += int(file_size)
    if len(d['dirs']):
        for dir in d['dirs']:
            total_file_size += calc_file_size(dirs[dir])
    pass
solve('sample.txt')
# solve('input.txt')
