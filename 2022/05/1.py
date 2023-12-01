def read_from_file(file):
    data = None
    with open(file) as f:
        data = f.read()
    return data

width_of_a_crate = 3

def 

# Takes in one row of the stacks portion of the input (doesn't matter which row)
# Determines how many stacks can fit in that row's width and returns that number
# So "[A] [B]    " returns 3 since 3 stacks can fit in that row's width
# So "[X] [Y]     [Z]    " returns 5 since 5 stacks can fit in that row's width
def determine_number_of_stacks(row):
    width_of_a_row = len(row)
    # Adding 1 to account for the space between crates
    number_of_stacks = (width_of_a_row + 1) // width_of_a_crate + 1
    return number_of_stacks

def solve(file):
    input_value = read_from_file(file)
    [crates_portion, instructions_portion] = input_value.split('\n\n')

    rows_of_crates = crates_portion.split('\n')[:-1] # Skip the last row which is labels
    number_of_stacks = determine_number_of_stacks(rows_of_crates[0])
    # Create empty stacks like {1: [], 2: [], 3: [], ...}
    stacks = {label: [] for label in range(1, number_of_stacks + 1)} 
    # print(stacks)
    for row in rows_of_crates:
        for index in range(0, len(row), width_of_a_crate):
            print(index)
        # print(crates_in_a_row)
        # for label in number_of_stacks

    # number_of_stacks = determine_number_of_stacks(input_value)
    # # Adding 1 to index because we want to start from 1 
    # all_stacks = {index + 1: [] for index in range(number_of_stacks)}
    # print(crates_portion)
    # print('========')
    # print(instructions_portion)
    # print(f'[{file}]: nothing')

solve('sample.txt')
# solve('input.txt')
