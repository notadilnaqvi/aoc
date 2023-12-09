def solve(file_path)
  document = File.open(file_path).read()

  instructions = document.split("\n\n")[0]
  maps = {}
  document.split("\n\n")[1].split("\n").each do |map|
    node = map.split(" = ")[0]
    lr = map.split(" = ")[1].gsub("(", "").gsub(")", "").split(", ")
    maps[node] = { "L" => lr[0], "R" => lr[1] }
  end

  current_node = "AAA"
  total_steps = 0

  while current_node != "ZZZ"
    direction = instructions[total_steps % instructions.length]
    current_node = maps[current_node][direction]
    total_steps += 1
  end

  print("[#{file_path}] #{total_steps}\n")

end

solve("sample-1.txt")
solve("sample-2.txt")
solve("input.txt")
