lines = File.read_lines("sample.txt")

password = 0
dial_starting_position = 50
max_dial_positions = 100
current_dial_position = dial_starting_position

lines.each_with_index do |rotation, i|
  direction = rotation[0]
  distance = rotation[1, rotation.size - 1].to_i

  rotations = distance // max_dial_positions
  password += rotations

  normalized_distance = distance % max_dial_positions # take mod to account for multiple rotations

  if direction == 'R'
    current_dial_position += normalized_distance
  elsif direction == 'L'
    current_dial_position -= normalized_distance
  else
    raise "invlaid direction"
  end

  new_dial_position = current_dial_position
  if current_dial_position < 0
    new_dial_position = max_dial_positions + current_dial_position
  elsif current_dial_position >= max_dial_positions
    new_dial_position = current_dial_position - max_dial_positions
  end

  if new_dial_position.sign != current_dial_position.sign || current_dial_position == 0
    password += 1
  end

  # puts "#{rotation} => #{current_dial_position}"

end

puts password

# 6835 low