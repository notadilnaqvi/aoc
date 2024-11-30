lines = File.read_lines("input.txt")

ans = nil

forward = 0
depth = 0
aim = 0

lines.each_with_index do |line, i|
  dir = line.split[0]
  units = line.split[1].to_i
  
  if dir == "forward"
    forward += units
    depth += (aim * units)
  elsif dir == "down"
    aim += units
  elsif dir == "up"
    aim -= units
  else
    raise "fuck"
  end
end

ans = forward * depth

puts ans
