def xy_from_index(index, col_count)
  return {
    "x" => (index % col_count),
    "y" => (index / col_count).floor
  }
end

def solve(file_path)
  file = File.open(file_path).read()

  rows = file.split("\n")
  row_count = rows.length
  col_count = rows[0].length

  rock_xys = []
  file.tr("\n", "").split("").each_with_index do |char, index|
    if char == "#"
      rock_xys.push(xy_from_index(index, col_count))
    end
  end

  # Rotate the whole thing clockwise (cols 🔁 rows) for easier manipulation
  # North is now East
  cols = []
  for y in 0..col_count - 1 do
    col = ''
    for x in 0..row_count - 1 do
      col = col + rows[x][y]
    end
    cols.push(col.each_char.to_a.reverse.join)
  end

  cols.each_with_index.map do |col, index|
    # print("#{index + 1}: #{col}\n")
    rock_indexes = col.each_char.to_a.each_with_index.map { |char, index| index if char == '#' }.filter { |index| index != nil }
    # print("#{col} --> #{rock_indexes} --> #{col.split("#")}\n")
    rock_indexes.map do |rock_index|
      print("#{rock_index},")
    end
    print("\n")
  end
end

solve('sample.txt')
