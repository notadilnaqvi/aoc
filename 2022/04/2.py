def read_from_file(file):
    data = None
    with open(file) as f:
        data = f.read()
    return data


# Converts "1-2" to {'start': 1, 'end': 2}
def determine_sections_range(elf):
    range_start = int(elf.split('-')[0])
    range_end = int(elf.split('-')[1])
    return {'start': range_start, 'end': range_end}


def solve(file):
    input_value = read_from_file(file)
    pairs = input_value.split('\n')
    number_of_pairs_that_have_any_overlap = 0
    for pair in pairs:
        [elf_1, elf_2] = pair.split(',')
        elf_1_range = determine_sections_range(elf_1)
        elf_2_range = determine_sections_range(elf_2)

        ranges_have_overlap = elf_1_range.get('start') <= elf_2_range.get('end') and elf_1_range.get('end') >= elf_2_range.get('start') 

        if(ranges_have_overlap):
            number_of_pairs_that_have_any_overlap += 1

    print(f'[{file}]: {number_of_pairs_that_have_any_overlap}')

solve('sample.txt')
solve('input.txt')
