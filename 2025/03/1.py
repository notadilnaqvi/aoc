def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

def solve(file_path: str) -> None:
  file_contents = read_from_file(file_path)

  battery_banks = file_contents.split('\n')
  total_joltage = 0

  for batter_bank in battery_banks:
    batteries = list(map(int, list(batter_bank)))
    max_battery_1 = max(batteries)
    batteries_right_of_max = batteries[batteries.index(max(batteries)) + 1:]
    batteries_left_of_max = batteries[:batteries.index(max(batteries))]

    max_battery_2 = None
    max_joltage = None

    if len(batteries_right_of_max) == 0:
      max_battery_2 = max(batteries_left_of_max)
      max_joltage = int(str(max_battery_2) + str(max_battery_1))
    else:
      max_battery_2 = max(batteries_right_of_max)
      max_joltage = int(str(max_battery_1) + str(max_battery_2))
    
    total_joltage += max_joltage

  print(total_joltage)
    

solve('input.txt')