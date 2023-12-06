sheet_of_paper = File.open("input.txt")

lines = sheet_of_paper.readlines

times = lines[0].split(" ").drop(1)
distances = lines[1].split(" ").drop(1)

races = []
times.zip(distances) do |time, distance|
  races.push({
    'time' => time.to_i,
    'distance' => distance.to_i,
  })
end

total_number_of_ways_to_win = 1

for race in races
  number_of_ways_to_win_for_current_race = 0
  for hold_time in 1..race['time'] - 1
    distance_covered = hold_time * (race['time'] - hold_time)
    if(distance_covered >= race['distance'])
      number_of_ways_to_win_for_current_race += 1
    end
  end
  total_number_of_ways_to_win *= number_of_ways_to_win_for_current_race
end

puts("[input.txt]: #{total_number_of_ways_to_win}")
