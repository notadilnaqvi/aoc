def read_from_file(file: str):
    data = None
    with open(file) as f:
        data = f.read()
    return data


def find_max_num(num_str):
    max_num = 0
    num_digits = len(num_str)

    for i in range(0, num_digits):
        for j in range(i + 1, num_digits):
            new_num = int(num_str[i] + num_str[j])
            if new_num > max_num:
                max_num = new_num

    return max_num


def solve(file_path: str) -> None:
    file_contents = read_from_file(file_path)

    battery_banks = file_contents.split('\n')
    total_joltage = 0

    total = 0
    for battery_bank in battery_banks:
        total += find_max_num(battery_bank)

    print(total)


solve('input.txt')
