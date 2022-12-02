OUTCOME_TO_SCORE_MAPPING = {
  'loss': 0,
  'draw': 3,
  'win': 6,
}

SHAPE_TO_SCORE_MAPPING = {
  # Rock
  'A': 1,
  'X': 1,
  # Paper
  'B': 2,
  'Y': 2,
  # Scissors
  'C': 3,
  'Z': 3,
}

def calculate_round_score(current_round):
  [opponent_shape, my_shape] = current_round.split(' ')
  shape_score = SHAPE_TO_SCORE_MAPPING.get(my_shape)
  outcome = calculate_outcome(opponent_shape, my_shape)
  outcome_score = OUTCOME_TO_SCORE_MAPPING.get(outcome)
  round_score = shape_score + outcome_score
  return round_score


def calculate_outcome(opponent_shape, my_shape):
  # My loss
  if opponent_shape == 'A' and my_shape == 'Z': return 'loss'
  if opponent_shape == 'B' and my_shape == 'X': return 'loss'
  if opponent_shape == 'C' and my_shape == 'Y': return 'loss'

  # My win
  if opponent_shape == 'A' and my_shape == 'Y': return 'win'
  if opponent_shape == 'B' and my_shape == 'Z': return 'win'
  if opponent_shape == 'C' and my_shape == 'X': return 'win'

  # Draw
  if opponent_shape == 'A' and my_shape == 'X': return 'draw'
  if opponent_shape == 'B' and my_shape == 'Y': return 'draw'
  if opponent_shape == 'C' and my_shape == 'Z': return 'draw'


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