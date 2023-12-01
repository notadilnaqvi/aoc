def read_from_file(file):
	data = None
	with open(file) as f:
		data = f.read()
	return data


def is_valid_digit(digit):
	try:
		int(digit)
		return True
	except ValueError:
		return False


def solve(file):
	calibration_document = read_from_file(file)
	lines = calibration_document.split('\n')
	
	calibration_value = 0

	for line in lines:
		all_digits_in_line = [int(letter) for letter in line if is_valid_digit(letter)]

		first_digit = all_digits_in_line[0]
		last_digit = first_digit if len(all_digits_in_line) == 1 else all_digits_in_line[-1]

		two_digit_number = int(f'{first_digit}{last_digit}')

		calibration_value = calibration_value + two_digit_number

	print(f'[{file}]: {calibration_value}')


solve('sample-1.txt')
solve('input.txt')
