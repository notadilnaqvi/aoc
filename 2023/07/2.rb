def determine_hand_type(original_hand)
  hash_of_original_hand = {}
  original_hand.split("").each do |card|
    if(hash_of_original_hand[card])
      hash_of_original_hand[card] += 1
    else
      hash_of_original_hand[card] = 1
    end
  end

  hand_with_J_replaced = original_hand

  if(hash_of_original_hand.has_key?("J") and hash_of_original_hand["J"] != 5)
    hash_of_original_hand.delete("J")
    max = hash_of_original_hand.max_by { |key, value| value }
    hand_with_J_replaced = original_hand.gsub("J", max[0])
  end

  hash_of_hand_with_J_replaced = {}
  hand_with_J_replaced.split("").each do |card|
    if(hash_of_hand_with_J_replaced[card])
      hash_of_hand_with_J_replaced[card] += 1
    else
      hash_of_hand_with_J_replaced[card] = 1
    end
  end

  if(hash_of_hand_with_J_replaced.length == 1)
    return { "strength" => 7, "name" => "five_of_a_kind" }
  end
  if(hash_of_hand_with_J_replaced.length == 2)
    if(hash_of_hand_with_J_replaced.has_value?(1))
      return { "strength" => 6, "name" => "four_of_a_kind" }
    end
    return { "strength" => 5, "name" => "full_house" }
  end
  if(hash_of_hand_with_J_replaced.length == 3)
    if(hash_of_hand_with_J_replaced.has_value?(3))
      return { "strength" => 4, "name" => "three_of_a_kind" }
    end
    return { "strength" => 3, "name" => "two_pair" }
  end
  if(hash_of_hand_with_J_replaced.length == 4)
    return { "strength" => 2, "name" => "one_pair" }
  end
  if(hash_of_hand_with_J_replaced.length == 5)
    return { "strength" => 1, "name" => "high_card" }
  end
end

def solve(file_path)
  hands_sorted_by_type = File.open(file_path).readlines(chomp: true).map { |hand_str| {"cards" => hand_str.split(" ")[0], "bet" => hand_str.split(" ")[1].to_i, "type" => determine_hand_type(hand_str.split(" ")[0])} }.sort_by { |hand| -hand["type"]["strength"] }

  hands_grouped_by_type_strength = hands_sorted_by_type.group_by { |hand| hand["type"]["strength"] }

  hands_sorted_by_type_and_strength = []
  for key in hands_grouped_by_type_strength.keys
    sorted_x = hands_grouped_by_type_strength[key].sort_by { |hand| hand["cards"].gsub('A', 'Z').gsub('K', 'Y').gsub('Q', 'X').gsub('J', '1').gsub('T', 'V') }.reverse
    for hand in sorted_x
      hands_sorted_by_type_and_strength.push(hand)
    end
  end

  total_winnings = hands_sorted_by_type_and_strength.map { |hand| hand["bet"] }.reverse.each_with_index.map { |bet, index| bet * (index + 1) }.sum

  print("[#{file_path}] #{total_winnings}\n")

end

solve("sample.txt")
solve("input.txt")
