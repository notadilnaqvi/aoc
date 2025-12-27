def read_from_file(file: str):
    data = None
    with open(file) as f:
        data = f.read()
    return data


def max_digit(num):
    return str(max(map(int, str(num))))

def find_max_num(num_str, required_digits):
    if required_digits== 1:
        return max_digit(num_str)
    
    # 1
    num_str_1 = num_str
    digit_1 = max_digit(num_str_1[:0 - (required_digits - 1)])
    digit_1_index = num_str.index(digit_1, 0)
    print("num_str_1:", num_str_1, "digit_1:", digit_1, "digit_1_index:", digit_1_index)

    # 2
    num_str_2 = num_str[digit_1_index + 1:]
    digit_2 = max_digit(num_str_2[:0 - (required_digits - 2)])
    digit_2_index = num_str.index(digit_2, digit_1_index + 1)
    print("num_str_2:", num_str_2, "digit_2:", digit_2, "digit_2_index:", digit_2_index)

    # 3
    num_str_3 = num_str[digit_2_index + 1:]
    digit_3 = max_digit(num_str_3[:0 - (required_digits - 3)])
    digit_3_index = num_str.index(digit_3, digit_2_index + 1)
    print("num_str_3:", num_str_3, "digit_3:", digit_3, "digit_3_index:", digit_3_index)

    # 4
    num_str_4 = num_str[digit_3_index + 1:]
    digit_4 = max_digit(num_str_4[:0 - (required_digits - 4)])
    digit_4_index = num_str.index(digit_4, digit_3_index + 1)
    print("num_str_4:", num_str_4, "digit_4:", digit_4, "digit_4_index:", digit_4_index)

    # 5
    num_str_5 = num_str[digit_4_index + 1:]
    digit_5 = max_digit(num_str_5[:0 - (required_digits - 5)])
    digit_5_index = num_str.index(digit_5, digit_4_index + 1)
    print("num_str_5:", num_str_5, "digit_5:", digit_5, "digit_5_index:", digit_5_index)

    # 6
    num_str_6 = num_str[digit_5_index + 1:]
    digit_6 = max_digit(num_str_6[:0 - (required_digits - 6)])
    digit_6_index = num_str.index(digit_6, digit_5_index + 1)
    print("num_str_6:", num_str_6, "digit_6:", digit_6, "digit_6_index:", digit_6_index)

    # 7
    num_str_7 = num_str[digit_6_index + 1:]
    digit_7 = max_digit(num_str_7[:0 - (required_digits - 7)])
    digit_7_index = num_str.index(digit_7, digit_6_index + 1)
    print("num_str_7:", num_str_7, "digit_7:", digit_7, "digit_7_index:", digit_7_index)

    # 8
    num_str_8 = num_str[digit_7_index + 1:]
    digit_8 = max_digit(num_str_8[:0 - (required_digits - 8)])
    digit_8_index = num_str.index(digit_8, digit_7_index + 1)
    print("num_str_8:", num_str_8, "digit_8:", digit_8, "digit_8_index:", digit_8_index)

    # 9
    num_str_9 = num_str[digit_8_index + 1:]
    digit_9 = max_digit(num_str_9[:0 - (required_digits - 9)])
    digit_9_index = num_str.index(digit_9, digit_8_index + 1)
    print("num_str_9:", num_str_9, "digit_9:", digit_9, "digit_9_index:", digit_9_index)

    # 10
    num_str_10 = num_str[digit_9_index + 1:]
    digit_10 = max_digit(num_str_10[:0 - (required_digits - 10)])
    digit_10_index = num_str.index(digit_10, digit_9_index + 1)
    print("num_str_10:", num_str_10, "digit_10:", digit_10, "digit_10_index:", digit_10_index)

    # 11
    num_str_11 = num_str[digit_10_index + 1:]
    digit_11 = max_digit(num_str_11[:0 - (required_digits - 11)])
    digit_11_index = num_str.index(digit_11, digit_10_index + 1)
    print("num_str_11:", num_str_11, "digit_11:", digit_11, "digit_11_index:", digit_11_index)
    
    # 12
    num_str_12 = num_str[digit_11_index + 1:]
    digit_12 = max_digit(num_str_12)
    digit_12_index = num_str.index(digit_12, digit_11_index + 1)
    print("num_str_12:", num_str_12, "digit_12:", digit_12, "digit_12_index:", digit_12_index)


    lol = digit_1 + digit_2 + digit_3 + digit_4 + digit_5 + digit_6 + digit_7 + digit_8 + digit_9 + digit_10 + digit_11 + digit_12

    return lol


def solve(file_path: str) -> None:
    file_contents = read_from_file(file_path)

    battery_banks = file_contents.split('\n')

    total = 0

    for battery_bank in battery_banks:
        total += int(find_max_num(battery_bank, 12))

    print(total)

solve('input.txt')

# 170023262301172 too high
