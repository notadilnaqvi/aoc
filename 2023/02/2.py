def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

def solve(file_path: str) -> None:
  file_contents = read_from_file(file_path)

  all_games = file_contents.split('\n')

  sum_of_powers_of_all_games = 0
  for game_str in all_games:
    [game_id, game] = game_str.split(': ')

    game_id = game_id.removeprefix('Game ')

    cube_reveals = game.split('; ')

    min_cube_count_required_for_current_game = {
      'red':  0,
      'green': 0,
      'blue': 0,
    }

    for cube_reveal in cube_reveals:
      revealed_cubes = cube_reveal.split(', ')
      
      for revealed_cube in revealed_cubes:
        [count, color] = revealed_cube.split(' ')
        if int(count) > min_cube_count_required_for_current_game[color]:
          min_cube_count_required_for_current_game[color] = int(count)

    power_of_current_game = 1
    for color in min_cube_count_required_for_current_game.keys():
      power_of_current_game *= min_cube_count_required_for_current_game[color]
   
    sum_of_powers_of_all_games += power_of_current_game

  print(f'[{file_path}]: {sum_of_powers_of_all_games}')

solve('sample.txt')
solve('input.txt')
