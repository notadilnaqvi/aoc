def read_from_file(file: str):
  data = None
  with open(file) as f:
    data = f.read()
  return data

def solve(file_path: str) -> None:
  file_contents = read_from_file(file_path)

  fresh_ingridient_id_ranges, _ingredient_ids = file_contents.split('\n\n')

  fresh_ingridient_id_ranges = [{"start": list(map(int,id_range.split('-')))[0], "end": list(map(int,id_range.split('-')))[1]} for id_range in fresh_ingridient_id_ranges.split('\n')]
  
  fresh_ingredient_ids_count = 0

  fresh_ingredient_ids_count_with_duplicates = 0
  seen_ranges_1 = []
  for fresh_ingridient_id_range in fresh_ingridient_id_ranges:
    if fresh_ingridient_id_range in seen_ranges_1:
      # print('found duplicate!',fresh_ingridient_id_range)
      continue
    seen_ranges_1.append(fresh_ingridient_id_range)
    fresh_ingredient_ids_count_with_duplicates += fresh_ingridient_id_range['end'] - fresh_ingridient_id_range['start'] + 1

  duplicates_count = 0
  seen_ranges_2 = []
  for i in range(0, len(fresh_ingridient_id_ranges)):
    first_range = fresh_ingridient_id_ranges[i]
    if first_range in seen_ranges_2:
      continue
    seen_ranges_2.append(first_range)
    seen_ranges_3 = []
    for j in range(i + 1, len(fresh_ingridient_id_ranges)):
      second_range = fresh_ingridient_id_ranges[j]

      if second_range in seen_ranges_3:
        continue

      seen_ranges_3.append(second_range)

      assert first_range['start'] <= first_range['end']
      assert second_range['start'] <= second_range['end']

      has_overlap = not (first_range['end'] < second_range['start'] or first_range['start'] > second_range['end'])

      if has_overlap:
        current_duplicates = min(first_range['end'], second_range['end']) - max(first_range['start'], second_range['start']) + 1
        duplicates_count += current_duplicates
        print(first_range, "overlaps with", second_range, "with", current_duplicates, "duplicates")

  print("total with duplicates:", fresh_ingredient_ids_count_with_duplicates)
  print("duplicates", duplicates_count)
  print("total", fresh_ingredient_ids_count_with_duplicates - duplicates_count)

solve('sample.txt')

# 267945376853099 too low
# 302824875278408 too low
# 358594099214401 incorrect
# 359846975509131 incorrect
# 1551787495952812607 high