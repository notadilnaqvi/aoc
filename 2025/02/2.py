import re

def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

def check_validity(id: int):
  id_str = str(id)

  return not bool(re.fullmatch(r"(.+)\1+", id_str))

  # # number with odd digits will only be invalid if all digits are the same
  # if len(id_str) % 2 != 0:
  #   return len(list(set(id_str))) != 1
  
  # first_half, second_half = id_str[:len(id_str)//2], id_str[len(id_str)//2:]
  # return first_half != second_half

def solve(file_path: str) -> None:
  file_contents = read_from_file(file_path)

  all_id_ranges = file_contents.split(',')

  invalid_ids_count = 0
  for id_range in all_id_ranges:
    [id_range_start, id_range_end] = map(int, id_range.split('-'))

    current_id = id_range_start

    while current_id <= id_range_end:
      is_valid = check_validity(current_id)

      if not is_valid:
        invalid_ids_count += current_id

      current_id += 1

  print(invalid_ids_count)

solve('input.txt')