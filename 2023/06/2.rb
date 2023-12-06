sheet_of_paper = File.open("input.txt")

lines = sheet_of_paper.readlines

time = lines[0].split(" ").drop(1).join.to_i
distance = lines[1].split(" ").drop(1).join.to_i

race = {
  'time' => time,
  'distance' => distance,
}

total_number_of_ways_to_win = 0

for hold_time in 1..race['time'] - 1
  distance_covered = hold_time * (race['time'] - hold_time)
  if(distance_covered >= race['distance'])
    total_number_of_ways_to_win += 1
  end
end

puts("[input.txt]: #{total_number_of_ways_to_win}")
