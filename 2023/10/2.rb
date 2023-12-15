# Determined manually
$starting_pipe_map = {
  "sample-1.txt" => "F",
  "sample-2.txt" => "F",
  "sample-3.txt" => "F",
  "sample-4.txt" => "F",
  "sample-5.txt" => "7",
  "input.txt" => "7"
}

# Determined manually
$previous_location_map = {
  "sample-1.txt" => { "x" => 2, "y" => 1},
  "sample-2.txt" => { "x" => 1, "y" => 2},
  "sample-3.txt" => { "x" => 2, "y" => 1},
  "sample-4.txt" => { "x" => 2, "y" => 1},
  "sample-5.txt" => { "x" => 4, "y" => 1},
  "input.txt" => { "x" => 25, "y" => 84}
}

def get_next_position(current_position, previous_position, type_of_pipe)

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

# https://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html
def is_point_inside_polygon(p, polygon)
  intersections_count = 0
  p1 = polygon[0]
  n = polygon.count

  # If point is on the polygon, it's not inside it
  if (p1["x"] == p["x"] and p1["y"] == p["y"])
    return false
  end

  for i in 1..n  do
    p2 = polygon[i % n]

    # If point is on the polygon, it's not inside it
    if (p2["x"] == p["x"] and p2["y"] == p["y"])
      return false
    end

    if p["y"] > [p1["y"], p2["y"]].min()
      if p["y"] <= [p1["y"], p2["y"]].max()
        if p["x"] <= [p1["x"], p2["x"]].max()
          if p1["y"] != p2["y"]
            x_intersection = (p["y"] - p1["y"]) * (p2["x"] - p1["x"]) / (p2["y"] - p1["y"]) + p1["x"]
            if (p1["x"] == p2["x"]) or (p["x"] <= x_intersection)
              intersections_count = intersections_count + 1
            end
          end
        end
      end
    end
    p1 = p2
  end

  return !(intersections_count % 2 == 0)
end

# https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
def is_point_inside_polygon_2(p, polygon)
  n = polygon.length
  j = n - 1
  c = false
  for i in 0..n-1
    if p["x"] == polygon[i]["x"] and p["y"] == polygon[i]["y"]
      return true
    end
    if (polygon[i]["y"] > p["y"]) != (polygon[j]["y"] > p["y"])
      slope =(p["x"] - polygon[i]["x"]) * (polygon[j]["y"] - polygon[i]["y"]) - (polygon[j]["x"] - polygon[i]["x"]) * (p["y"] - polygon[i]["y"])
      if slope == 0
        return true
      end
      if (slope < 0) != (polygon[j]["y"] < polygon[i]["y"])
        c = !c
      end
    end
    j = i
  end
  return c
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

  polygon = []
  while current_pipe != "S"
    next_position = get_next_position(current_position, previous_position, current_pipe)
    # if current_pipe != "-" and current_pipe != "|"
    polygon.push(current_position)
    # end
    previous_position = current_position
    current_position = next_position
    current_pipe = rows[current_position["y"]][current_position["x"]]
  end

  inside_points = []
  for y in 0..row_count-1 do
    for x in 0..col_count-1 do
      p = {
        "x" => x,
        "y" => y
      }
      if is_point_inside_polygon(p, polygon) == true
        inside_points.push(rows[y][x])
      end
    end
  end

  print("[#{file_path}]: #{inside_points.length}\n")

end

solve("sample-1.txt")
solve("sample-2.txt")
solve("sample-3.txt")
solve("sample-4.txt")
solve("sample-5.txt")
solve("input.txt") # Takes about 30s
