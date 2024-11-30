lines = File.read_lines("input.txt")

ans = 0

lines.each_with_index do |_, i|
  if lines[i].to_i > lines[i - 1].to_i
    ans += 1
  end
end

puts ans