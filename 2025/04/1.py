def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

#   -1  0  1
#  1 a  b  c
#  0 g  x  d
# -1 g  f  e
dirs = [
  [-1, 1], # a
  [ 0, 1], # b
  [ 1, 1], # c
  [ 1, 0], # d
  [ 1,-1], # e
  [ 0,-1], # f
  [-1,-1], # g
  [-1, 0], # h
]

def solve(file_path: str) -> None:
  file_contents = read_from_file(file_path)

  rows = list(map(list, file_contents.split('\n')))

  accessible_by_forklift = 0
  for y, row in enumerate(rows):
    for x, col in enumerate(row):
      if (col != '@'):
        continue
      neighbours = []
      for dir in dirs:
        neighbour_x = x + dir[0]
        neighbour_y = y + dir[1]
        if neighbour_x < 0 or neighbour_x >= len(rows[0]) or neighbour_y < 0 or neighbour_y >= len(rows):
          continue
        else:
          neighbours.append(rows[neighbour_y][neighbour_x])

      if neighbours.count('@') < 4:
        accessible_by_forklift += 1

  print(accessible_by_forklift)

solve('input.txt')