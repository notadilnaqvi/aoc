def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

DIGITS_MAP = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

def is_spelled_out_digit(digit: str):
  return digit in DIGITS_MAP.keys()

def is_numeric_digit(digit: str):
  return digit in DIGITS_MAP.values()

# 'asdffivexyz' -> 'five'
def contains_which_spelled_out_digit(string: str):
  for spelled_out_digit in DIGITS_MAP.keys():
    if spelled_out_digit in string:
      return spelled_out_digit
    continue
  return None

# 'asdf5xyz' -> '5'
def contains_which_numeric_digit(string: str):
  for numeric_digit in DIGITS_MAP.values():
    if numeric_digit in string:
      return numeric_digit
    continue
  return None

# 'five' -> 5
def convert_spelled_out_digit_to_numeric_digit(spelled_out_digit: str):
  try:
    int(spelled_out_digit)
    return spelled_out_digit
  except ValueError:
    if spelled_out_digit in DIGITS_MAP.keys():
      return DIGITS_MAP[spelled_out_digit]
    return None


def solve(file_path: str) -> None:
  calibration_document = read_from_file(file_path)
  
  lines = calibration_document.split('\n')

  sum_of_calibration_values = 0

  # Find the first digit
  for line in lines:
    first_digit = None
    first_digit_window = ''
    for letter in line:
      first_digit_window = first_digit_window + letter
      contained_numeric_digit = contains_which_numeric_digit(first_digit_window)
      contained_spelled_out_digit = contains_which_spelled_out_digit(first_digit_window)
      if contained_numeric_digit:
        first_digit = contained_numeric_digit
        break
      elif contained_spelled_out_digit:
        first_digit = convert_spelled_out_digit_to_numeric_digit(contained_spelled_out_digit)
        break
      else:
        pass

    # Find the last digit
    last_digit = None
    last_digit_window = ''
    for letter in line[::-1]:
      last_digit_window = last_digit_window + letter
      contained_numeric_digit = contains_which_numeric_digit(last_digit_window[::-1])
      contained_spelled_out_digit = contains_which_spelled_out_digit(last_digit_window[::-1])
      if contained_numeric_digit:
        last_digit = contained_numeric_digit
        break
      elif contained_spelled_out_digit:
        last_digit = convert_spelled_out_digit_to_numeric_digit(contained_spelled_out_digit)
        break
      else:
        pass

    calibration_value = int(f'{first_digit}{last_digit}')
    sum_of_calibration_values = sum_of_calibration_values + calibration_value

  print(f'[{file_path}]: {sum_of_calibration_values}')

solve('sample-1.txt')
solve('sample-2.txt')
solve('input.txt')
