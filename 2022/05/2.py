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

        # Instead of checking if the ranges overlap, we check if they don't overlap and invert the result
        # There are only 2 ways for range 1 to NOT overlap with range 2.
        # 1. Range 1 is completely to the left of range 2 (i.e. range 2's start is greater than range 1's end) ------- [range 1] [range 2]
        # 2. Range 1 is completely to the right of range 2 (i.e. range 2's end is less than range 1's start) --------- [range 2] [range 1]
        ranges_have_overlap = not (elf_2_range.get('start') > elf_1_range.get('end') or elf_2_range.get('end') < elf_1_range.get('start'))

        if(ranges_have_overlap):
            number_of_pairs_that_have_any_overlap += 1

    print(f'[{file}]: {number_of_pairs_that_have_any_overlap}')

solve('sample.txt')
solve('input.txt')
