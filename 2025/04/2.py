def read_from_file(file: str):
    data = None
    with open(file) as f:
        data = f.read()
    return data


#   -1  0  1
#  1 a  b  c
#  0 h  x  d
# -1 g  f  e
directions = [
    [-1, 1],  # a
    [0, 1],  # b
    [1, 1],  # c
    [1, 0],  # d
    [1, -1],  # e
    [0, -1],  # f
    [-1, -1],  # g
    [-1, 0],  # h
]


def get_neighbours(x, y, grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    neighbours = []
    for direction in directions:
        neighbour_x = x + direction[0]
        neighbour_y = y + direction[1]
        if neighbour_x < 0 or neighbour_x >= num_cols or neighbour_y < 0 or neighbour_y >= num_rows:
            continue
        else:
            neighbours.append(grid[neighbour_x][neighbour_y])

    return neighbours


def is_roll_accessible_by_forklift(roll_x, roll_y, grid):
    neighbours = get_neighbours(roll_x, roll_y, grid)
    return neighbours.count('@') < 4


def remove_rolls(rolls, grid):
    new_grid = grid

    for roll in rolls:
        x, y = roll
        # assert new_grid[x][y] == "@"
        new_grid[x][y] = "."

    return new_grid


def solve(file_path: str) -> None:
    file_contents = read_from_file(file_path)

    grid = list(map(list, file_contents.split('\n')))

    num_rows = len(grid)
    num_cols = len(grid[0])

    rolls_to_remove = []

    flag = True
    while(flag):
      some_rolls_accessible_by_forklift = False
      for x in range(num_cols):
          for y in range(num_rows):
              roll = grid[x][y]
              if roll != "@":
                  continue
              if is_roll_accessible_by_forklift(x, y, grid):
                  some_rolls_accessible_by_forklift = True
                  rolls_to_remove.append([x,y])

      new_grid = remove_rolls(rolls_to_remove, grid)

      grid = new_grid

      if not some_rolls_accessible_by_forklift:
          flag = False
          print(len(rolls_to_remove))

solve('input.txt')
