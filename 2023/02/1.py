def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

total_cube_counts = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

def solve(file_path: str) -> None:
  file_contents = read_from_file(file_path)

  all_games = file_contents.split('\n')

  ids_of_possible_games = []
  for game_str in all_games:
    [game_id, game] = game_str.split(': ')

    game_id = game_id.removeprefix('Game ')

    cube_reveals = game.split('; ')

    is_game_valid = True
    for cube_reveal in cube_reveals:
      revealed_cubes = cube_reveal.split(', ')
      
      for revealed_cube in revealed_cubes:
        [count, color] = revealed_cube.split(' ')
        if int(count) > total_cube_counts[color]:
          is_game_valid = False
          break
    
      # No need to check other cube reveals if even one reveal is invalid
      if not is_game_valid:
        break

    if is_game_valid:
      ids_of_possible_games.append(int(game_id))

      

  print(f'[{file_path}]: {sum(ids_of_possible_games)}')

solve('sample.txt')
solve('input.txt')
