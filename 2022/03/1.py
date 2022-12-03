def read_from_file(file):
  data = None
  with open(file) as f:
    data = f.read()
  return data

def get_rucksack_compartments(rucksack):
  # Each rucksack will have an even number of items
  # Both compartments will have the same number of items
  compartment_1 = rucksack[:len(rucksack)//2]
  compartment_2 = rucksack[len(rucksack)//2:]
  return [compartment_1, compartment_2]

def find_common_item(compartment_1, compartment_2):
  # There will only be a single common item
  for item in compartment_1:
    if item in compartment_2:
      return item
  return None

def get_item_priority(item):
  # ASCII table: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
  is_uppercase = item.isupper()
  if is_uppercase:
    # 'A' in ASCII is 65, 'A' in the problem is 27, the difference is 38
    return ord(item) - 38
  # 'a' in ASCII is 97, 'a' in the problem is 1, difference is 96
  return ord(item) - 96

def solve(file):
  input_value = read_from_file(file)
  rucksacks = input_value.split('\n')
  sum_of_common_item_priorities = 0
  for rucksack in rucksacks:
    [compartment_1, compartment_2] = get_rucksack_compartments(rucksack)
    common_item = find_common_item(compartment_1, compartment_2)
    common_item_priority = get_item_priority(common_item)
    sum_of_common_item_priorities += common_item_priority
  
  print(f'[{file}]: {sum_of_common_item_priorities}')

solve('sample.txt')
solve('input.txt')