def solve(file_path)
  document = File.open(file_path).read()

  instructions = document.split("\n\n")[0]
  maps = {}
  document.split("\n\n")[1].split("\n").each do |map|
    node = map.split(" = ")[0]
    lr = map.split(" = ")[1].gsub("(", "").gsub(")", "").split(", ")
    maps[node] = { "L" => lr[0], "R" => lr[1] }
  end


  current_nodes = maps.keys.select { |node| node[-1] == "A" }

  # Each node eventually leads to a node with "Z" and then loops over
  # We find the number of steps for each node to reach "Z" and then
  # find the least common multiple of all those numbers becasue that's
  # when all the initial nodes will reach "Z" at the same time

  steps_for_each_node = []
  for current_node in current_nodes
    steps_for_current_node = 0
    while current_node[-1] != "Z"
      direction = instructions[steps_for_current_node % instructions.length]
      current_node = maps[current_node][direction]
      steps_for_current_node += 1
    end
    steps_for_each_node.push(steps_for_current_node)
  end
  lcm = steps_for_each_node.reduce(1, :lcm)
  print("[#{file_path}] #{lcm}\n")

end

solve("sample-3.txt")
solve("input.txt")
