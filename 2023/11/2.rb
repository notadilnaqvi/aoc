def xy_from_index(index, col_count)
  return {
    "x" => (index % col_count),
    "y" => (index / col_count).floor
  }
end

# Subtract 1 because one unit was already counted in x_diff/y_diff
# $expansion_factor = 2 - 1
# $expansion_factor = 10 - 1
# $expansion_factor = 100 - 1
$expansion_factor = 1000000 - 1

def get_dist_after_expansion(p1, p2, cols_with_no_galaxies, rows_with_no_galaxies)

  x_diff = p1["x"] - p2["x"]
  y_diff = p1["y"] - p2["y"]

  expanded_cols_offset = 0
  cols_with_no_galaxies.each do |col|
    if p1["x"] < p2["x"] and p1["x"] < col and col < p2["x"]
      # print(" col: #{col} is between #{p1["x"]} and #{p2["x"]}\n")
      expanded_cols_offset = expanded_cols_offset + $expansion_factor
    elsif p2["x"] < p1["x"] and p2["x"] < col and col < p1["x"]
      # print(" col: #{col} is between #{p2["x"]} and #{p1["x"]}\n")
      expanded_cols_offset = expanded_cols_offset + $expansion_factor
    else
      # print(" col: #{col} is NOT between #{p2["x"]} and #{p1["x"]}\n")
    end
  end

  expanded_rows_offset = 0
  rows_with_no_galaxies.each do |row|
    if p1["y"] < p2["y"] and p1["y"] < row and row < p2["y"]
      # print(" row: #{row} is between #{p1["y"]} and #{p2["y"]}\n")
      expanded_rows_offset = expanded_rows_offset + $expansion_factor
    elsif p2["y"] < p1["y"] and p2["y"] < row and row < p1["y"]
      # print(" row: #{row} is between #{p2["y"]} and #{p1["y"]}\n")
      expanded_rows_offset = expanded_rows_offset + $expansion_factor
    else
      # print(" row: #{row} is NOT between #{p2["y"]} and #{p1["y"]}\n")
    end
  end
  # print("dist: #{x_diff.abs} + #{y_diff.abs} + #{expanded_rows_offset} + #{expanded_cols_offset}\n\n")
  dist =  x_diff.abs + y_diff.abs + expanded_rows_offset + expanded_cols_offset
  return dist
end

def solve(file_path)
  image = File.open(file_path).read()

  rows = image.split("\n")

  row_count = rows.length
  col_count = rows[0].length

  galaxy_indexes = (0 ... image.tr("\n", '').length).find_all { |i| image.tr("\n", '')[i,1] == '#' }
  galaxy_xys = []
  galaxy_indexes.each do |index|
    galaxy_xys.push(xy_from_index(index, col_count))
  end

  rows_with_no_galaxies = rows.each_with_index.map { |row, index| index if not row.include?('#') }.filter { |index| index != nil }

  cols_with_no_galaxies = []
  for x in 0..col_count - 1 do
    current_col_has_galaxy = false
    for y in 0..row_count - 1 do
      if (rows[y][x] == '#')
        current_col_has_galaxy = true
        break
      end
    end
    if not current_col_has_galaxy
      cols_with_no_galaxies.push(x)
    end
  end

  total_dist = 0
  for i in 0..galaxy_xys.length - 1 do
    p1 = galaxy_xys[i]
    for j in i..galaxy_xys.length - 1 do
      if i != j
        p2 = galaxy_xys[j]
        # print("p#{i + 1}: #{p1}\n")
        # print("p#{j + 1}: #{p2}\n")
        dist = get_dist_after_expansion(p1, p2, cols_with_no_galaxies, rows_with_no_galaxies)
        total_dist = total_dist + dist
      end
    end
  end

  print("[#{file_path}]: #{total_dist}\n")
end

solve('sample.txt')
solve('input.txt')
