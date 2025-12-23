def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

def solve(file_path: str) -> None:
  file_contents = read_from_file(file_path)

  fresh_ingridient_id_ranges, ingredient_ids = file_contents.split('\n\n')

  fresh_ingridient_id_ranges = [list(map(int,id_range.split('-'))) for id_range in fresh_ingridient_id_ranges.split('\n')]

  ingredient_ids = [int(ingredient_id) for ingredient_id in ingredient_ids.split('\n')]
  
  fresh_ingredient_ids_count = 0

  for ingredient_id in ingredient_ids:
    is_fresh = False
    for fresh_ingridient_id_range in fresh_ingridient_id_ranges:
      range_min, range_max = fresh_ingridient_id_range
      if ingredient_id >= range_min and ingredient_id <= range_max:
        is_fresh = True
      
      if is_fresh:
        break

    if is_fresh:
      fresh_ingredient_ids_count += 1

  print(fresh_ingredient_ids_count)

solve('input.txt')