import math

def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

def solve(file_path: str) -> None:
  file_contents = read_from_file(file_path)

  rows = file_contents.split('\n')

  proplems = []
  for row in rows:
    numbers_or_operations = row.split()
    for i, number_or_operation in enumerate(numbers_or_operations):
      if i >= len(proplems):
        proplems.append([])
      proplems[i].append(number_or_operation)

  answers_sum = 0
  for proplem in proplems:
    numbers = list(map(int, proplem[:-1]))
    operation = proplem[-1]

    ans = None
    if operation == "*":
      ans = math.prod(numbers)
    elif operation == "+":
      ans = sum(numbers)
    else:
      raise "invalid operation"
    
    answers_sum += ans

  print(answers_sum)



solve('input.txt')