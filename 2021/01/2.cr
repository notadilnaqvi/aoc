lines = File.read_lines("input.txt")

ans = 0
window = 3

lines.each_with_index do |_, i|
  # Stop when there aren't enough measurements left to create a new three-measurement sum
  if i + window > lines.size
    break
  end

  cws = 0
  pws = 0

  Array.new(window, nil).each_with_index do |_, j|
    cws += lines[i + j].to_i
    pws += lines[i + j - 1].to_i
  end

  if cws > pws
    ans += 1
  end
end

puts ans