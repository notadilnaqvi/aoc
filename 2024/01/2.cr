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

rl.each_with_index do |rn, i|
  times = 0
  ll.each do |ln|
    if rn == ln
      times += 1
    end
  end
  ans += rn * times
end

puts ans