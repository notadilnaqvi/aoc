OUTCOME_TO_SCORE_MAPPING = {
  'X': 0, # Loss
  'Y': 3, # Draw
  'Z': 6, # Win
}

SHAPE_TO_SCORE_MAPPING = {
  'A': 1, # Rock
  'B': 2, # Paper
  'C': 3, # Scissors
}

def calculate_round_score(current_round):
  [opponent_shape, outcome] = current_round.split(' ')
  my_shape = calculate_my_shape(opponent_shape, outcome)
  shape_score = SHAPE_TO_SCORE_MAPPING.get(my_shape)
  outcome_score = OUTCOME_TO_SCORE_MAPPING.get(outcome)
  round_score = shape_score + outcome_score
  return round_score


def calculate_my_shape(opponent_shape, outcome):
  # My loss
  if opponent_shape == 'A' and outcome == 'X': return 'C'
  if opponent_shape == 'B' and outcome == 'X': return 'A'
  if opponent_shape == 'C' and outcome == 'X': return 'B'

  # Draw
  if opponent_shape == 'A' and outcome == 'Y': return 'A'
  if opponent_shape == 'B' and outcome == 'Y': return 'B'
  if opponent_shape == 'C' and outcome == 'Y': return 'C'

  # My win
  if opponent_shape == 'A' and outcome == 'Z': return 'B'
  if opponent_shape == 'B' and outcome == 'Z': return 'C'
  if opponent_shape == 'C' and outcome == 'Z': return 'A'


def solve(input_value):
    rounds = input_value.splitlines()
    total_score = 0
    for current_round in rounds:
      round_score = calculate_round_score(current_round)
      total_score += round_score
        
    return total_score

FILES = ['sample.txt', 'input.txt']
try:
  for file in FILES:
    with open(file) as f:
      input_value = f.read()
      solution = solve(input_value)
      print(f'[{file}]:', solution)
except Exception as e:
  print('[error]', e)