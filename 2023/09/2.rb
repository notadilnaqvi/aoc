def get_next_sequence(sequence)
  next_sequence = []
  for index in (0..sequence.length - 2) do
    difference = sequence[index + 1] - sequence[index]
    next_sequence.push(difference)
  end
  return next_sequence
end

def solve(file_path)
  histories = File.open(file_path).readlines()

  value_of_all_histories = 0
  for current_history in histories do
    current_sequence = current_history.split(" ").map { |value| value.to_i }

    all_sequences = []
    while not current_sequence.all? { |value| value == 0 } do
      all_sequences.push(current_sequence)
      current_sequence = get_next_sequence(current_sequence)
    end

    value_of_current_history = 0
    for sequence in all_sequences.reverse do
      value_of_current_history = sequence[0] - value_of_current_history
    end
    value_of_all_histories+=value_of_current_history
  end
  print("[#{file_path}]: #{value_of_all_histories}\n")

end


solve("sample.txt")
solve("input.txt")
