import math

def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)


def solve(file_path: str) -> None:
  instructions = read_from_file(file_path).split('\n')
  starting_position = 50
  max_positions = 100

  dial = list(range(max_positions))

  password = 0
  current_position = starting_position
  for instruction in instructions:
    direction = instruction[0]
    distance = int(instruction[1:])

    all_positions_in_current_instruction = None
    if direction == "R":
      all_positions_in_current_instruction = [dial[(i + current_position) % max_positions] for i in range(1, distance + 1)]
    elif direction == "L":
      all_positions_in_current_instruction = [dial[(current_position - i) % max_positions] for i in range(1, distance + 1)]
    else:
      raise "invalid direction"
    
    password =  password + all_positions_in_current_instruction.count(0)
    current_position = all_positions_in_current_instruction[-1]
  
  print(password)


solve('input.txt')