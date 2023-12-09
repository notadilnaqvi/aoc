def determine_hand_type(hand)
  hash = {}
  hand.split("").each do |card|
    if(hash[card])
      hash[card] += 1
    else
      hash[card] = 1
    end
  end

  if(hash.length == 1)
    return { "strength" => 7, "name" => "five_of_a_kind" }
  end
  if(hash.length == 2)
    if(hash.has_value?(1))
      return { "strength" => 6, "name" => "four_of_a_kind" }
    end
    return { "strength" => 5, "name" => "full_house" }
  end
  if(hash.length == 3)
    if(hash.has_value?(3))
      return { "strength" => 4, "name" => "three_of_a_kind" }
    end
    return { "strength" => 3, "name" => "two_pair" }
  end
  if(hash.length == 4)
    return { "strength" => 2, "name" => "one_pair" }
  end
  if(hash.length == 5)
    return { "strength" => 1, "name" => "high_card" }
  end
end

def solve(file_path)
  hands_sorted_by_type = File.open(file_path).readlines(chomp: true).map { |hand_str| {"cards" => hand_str.split(" ")[0], "bet" => hand_str.split(" ")[1].to_i, "type" => determine_hand_type(hand_str.split(" ")[0])} }.sort_by { |hand| -hand["type"]["strength"] }

  hands_grouped_by_type_strength = hands_sorted_by_type.group_by { |hand| hand["type"]["strength"] }

  hands_sorted_by_type_and_strength = []
  for key in hands_grouped_by_type_strength.keys
    sorted_hands_grouped_by_type_strength = hands_grouped_by_type_strength[key].sort_by { |hand| hand["cards"].gsub('A', 'Z').gsub('K', 'Y').gsub('Q', 'X').gsub('J', 'W').gsub('T', 'V') }.reverse
    for hand in sorted_hands_grouped_by_type_strength
      hands_sorted_by_type_and_strength.push(hand)
    end
  end

  total_winnings = hands_sorted_by_type_and_strength.map { |hand| hand["bet"] }.reverse.each_with_index.map { |bet, index| bet * (index + 1) }.sum

  print("[#{file_path}] #{total_winnings}\n")

end

solve("sample.txt")
solve("input.txt")
