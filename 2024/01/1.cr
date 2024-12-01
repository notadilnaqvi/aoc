lines = File.read_lines("input.txt")

ans = 0

rl = [] of Int32
ll = [] of Int32

lines.each_with_index do |line, i|
  rn = line.split[0].to_i
  ln = line.split[1].to_i
  rl << rn
  ll << ln
end

srl = rl.sort { |a, b| a <=> b }
sll = ll.sort { |a, b| a <=> b }

srl.each_with_index do |n, i|
  d = n - sll[i]
  ans += d.abs
end

puts ans