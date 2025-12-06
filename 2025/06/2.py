import re
import math


def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

def solve(file_path: str) -> None:
  file_contents = read_from_file(file_path)

  rows = file_contents.split('\n')
  numbers = rows[:-1]
  operations = rows[-1]

  matches = re.findall("[\\*|\\+]\\s+", operations)

  widths = [len(match) if i == len(matches)-1 else len(match)-1 for i, match in enumerate(matches)]



  proplems = []
  for row in rows:
    pointer = 0
    for wi,width in enumerate(widths):
      if wi >= len(proplems):
        proplems.append([])
      proplems[wi].append(row[pointer:pointer+width])
      pointer += width + 1

  answers_sum = 0
  for problem in reversed(proplems):
    new_numbers = []
    numbers = problem[:-1]
    operation = problem[-1].strip()
    for number in numbers:
      for di, digit in enumerate(number):
        new_numbers.append('')
        new_numbers[di] += digit
    
    new_numbers = list(map(int,list(filter(None,[s.strip() for s in new_numbers]))))
    
    ans = None
    if operation == "*":
      ans = math.prod(new_numbers)
    elif operation == "+":
      ans = sum(new_numbers)
    else:
      raise "invalid operation"
    
    answers_sum += ans

  print(answers_sum)
    
  
solve('input.txt')

# numbers = ['64 ', '23 ', '314']

# new_numbers = []
# for number in numbers:
#   for di,digit in enumerate(number):
#     new_numbers.append('')
#     new_numbers[di] += digit

# print(new_numbers)