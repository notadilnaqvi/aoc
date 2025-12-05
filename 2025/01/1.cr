lines = File.read_lines("input.txt")

password = 0
dial_starting_position = 50
max_dial_positions = 100
current_dial_position = dial_starting_position

lines.each_with_index do |rotation, i|
  direction = rotation[0]
  distance = rotation[1, rotation.size - 1].to_i % max_dial_positions # take mod to account for multiple rotations

  if direction == 'R'
    current_dial_position += distance
  elsif direction == 'L'
    current_dial_position -= distance
  else
    raise "invlaid direction"
  end

  if current_dial_position < 0
    current_dial_position = max_dial_positions + current_dial_position
  elsif current_dial_position >= max_dial_positions
    current_dial_position = current_dial_position - max_dial_positions
  end
  
  if current_dial_position == 0
    password += 1
  end
end

puts password