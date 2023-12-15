$pretty_map = {
  "F" => "┌",
  "-" => "─",
  "7" => "┐",
  "|" => "│",
  "J" => "┘",
  "L" => "└",
}

# Determined manually
$starting_pipe_map = {
  "sample-1.txt" => "F",
  "sample-2.txt" => "F",
  "input.txt" => "7"
}

# Determined manually
$previous_location_map = {
  "sample-1.txt" => { "x" => 2, "y" => 1},
  "sample-2.txt" => { "x" => 1, "y" => 2},
  "input.txt" => { "x" => 25, "y" => 84}
}

def get_next_position(current_position, previous_position, type_of_pipe)

  if false
    puts "┌ ─ ┐       F - 7"

    puts "│   │  ==>  |   |"

    puts "└ ─ ┘       L - J"
  end

  next_position = {
    "x" => nil,
    "y" => nil
  }

  if type_of_pipe == "F"
    if current_position["x"] == previous_position["x"]
      next_position["x"] = current_position["x"] + 1
      next_position["y"] = current_position["y"]
    elsif current_position["y"] == previous_position["y"]
      next_position["x"] = current_position["x"]
      next_position["y"] = current_position["y"] + 1
    else
      raise "haww hayee"
    end

  elsif  type_of_pipe == "-"
    if current_position["x"] < previous_position["x"]
      next_position["x"] = current_position["x"] - 1
      next_position["y"] = current_position["y"]
    elsif current_position["x"] > previous_position["x"]
      next_position["x"] = current_position["x"] + 1
      next_position["y"] = current_position["y"]
    else
      raise "haww hayee"
    end
  elsif  type_of_pipe == "7"
    if current_position["x"] == previous_position["x"]
      next_position["x"] = current_position["x"] - 1
      next_position["y"] = current_position["y"]
    elsif current_position["y"] == previous_position["y"]
      next_position["x"] = current_position["x"]
      next_position["y"] = current_position["y"] + 1
    else
      raise "haww hayee"
    end
  elsif  type_of_pipe == "|"
    if current_position["y"] < previous_position["y"]
      next_position["x"] = current_position["x"]
      next_position["y"] = current_position["y"] - 1
    elsif current_position["y"] > previous_position["y"]
      next_position["x"] = current_position["x"]
      next_position["y"] = current_position["y"] + 1
    else
      raise "haww hayee"
    end
  elsif  type_of_pipe == "J"
    if current_position["x"] == previous_position["x"]
      next_position["x"] = current_position["x"] - 1
      next_position["y"] = current_position["y"]
    elsif current_position["y"] == previous_position["y"]
      next_position["x"] = current_position["x"]
      next_position["y"] = current_position["y"] - 1
    else
      raise "haww hayee"
    end
  elsif  type_of_pipe == "L"
    if current_position["x"] == previous_position["x"]
      next_position["x"] = current_position["x"] + 1
      next_position["y"] = current_position["y"]
    elsif current_position["y"] == previous_position["y"]
      next_position["x"] = current_position["x"]
      next_position["y"] = current_position["y"] - 1
    else
      raise "haww hayee"
    end
  else
    raise "haww hayee"
  end

  return next_position
end

def solve(file_path)

  diagram = File.open(file_path).read()

  rows = diagram.split("\n")

  row_count = rows.length
  col_count = rows[0].length

  start_index = /S/.match(diagram.gsub("\n", "")).begin(0)

  starting_position = {
    "x" => (start_index % col_count),
    "y" => (start_index / col_count).floor
  }

  starting_pipe = $starting_pipe_map[file_path]

  current_position = starting_position

  current_pipe = starting_pipe

  previous_position = $previous_location_map[file_path]

  steps = 0
  while current_pipe != "S"
    next_position = get_next_position(current_position, previous_position, current_pipe)
    previous_position = current_position
    current_position = next_position
    current_pipe = rows[current_position["y"]][current_position["x"]]
    steps += 1
  end

  print("[#{file_path}]: #{steps/2}\n")

end

solve("sample-1.txt")
solve("sample-2.txt")
solve("input.txt")
