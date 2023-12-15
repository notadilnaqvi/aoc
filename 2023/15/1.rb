def calculate_hash(string)
  ascii_codes = string.codepoints
  hash = 0
  for ascii_code in ascii_codes
    hash = hash + ascii_code
    hash = hash * 17
    hash = hash % 256
  end
  return hash
end

def solve(file_path)

  initialization_sequence = File.open(file_path).read()

  steps = initialization_sequence.split(',')

  hash_value = 0

  for current_step in steps
    hash_of_current_step = calculate_hash(current_step)
    hash_value = hash_value + hash_of_current_step
  end

  print("[#{file_path}]: #{hash_value}\n")
end

solve("sample-1.txt")
solve("sample-2.txt")
solve("input.txt")
