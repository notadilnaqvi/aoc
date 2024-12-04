lines = File.read_lines("input.txt")

ans = 0

grid = [] of Array(String)
lines.each_with_index do |row, i|
  line_chars = row.split("")
  row = [] of String
  line_chars.each_with_index do |char, j|
    row << char
  end
  grid << row
end

def check(curr_y, curr_x, grid)
  count = 0
  row_n = grid.size
  col_n = grid[0].size

  # Horizontal
  if (curr_x + 3 < col_n && curr_x + 2 < col_n && curr_x + 1 < col_n)
    if (grid[curr_y][curr_x] == "X" && grid[curr_y][curr_x + 1] == "M" && grid[curr_y][curr_x + 2] == "A" && grid[curr_y][curr_x + 3] == "S")
      count += 1
    end
  end

  if (curr_x - 3 >= 0 && curr_x - 2 >= 0 && curr_x - 1 >= 0)
    if (grid[curr_y][curr_x] == "X" && grid[curr_y][curr_x - 1] == "M" && grid[curr_y][curr_x - 2] == "A" && grid[curr_y][curr_x - 3] == "S")
      count += 1
    end
  end
  
  # Vertical
  if (curr_y + 3 < row_n && curr_y + 2 < row_n && curr_y + 1 < row_n)
    if (grid[curr_y][curr_x] == "X" && grid[curr_y + 1][curr_x] == "M" && grid[curr_y + 2][curr_x] == "A" && grid[curr_y + 3][curr_x] == "S")
      count += 1
    end
  end

  if (curr_y - 3 >= 0 && curr_y - 1 >= 0 && curr_y - 1 >= 0)
    if (grid[curr_y][curr_x] == "X" && grid[curr_y - 1][curr_x] == "M" && grid[curr_y - 2][curr_x] == "A" && grid[curr_y - 3][curr_x] == "S")
      count += 1
    end
  end
  
  # Diagonal 
  if (curr_y + 3 < row_n && curr_y + 2 < row_n && curr_y + 1 < row_n && curr_x + 3 < col_n && curr_x + 2 < col_n && curr_x + 1 < col_n)
    if (grid[curr_y][curr_x] == "X" && grid[curr_y + 1][curr_x + 1] == "M" && grid[curr_y + 2][curr_x + 2] == "A" && grid[curr_y + 3][curr_x + 3] == "S")
      count += 1
    end
  end


  if (curr_y - 3 >= 0 && curr_y - 1 >= 0 && curr_y - 1 >= 0 && curr_x - 3 >= 0 && curr_x - 2 >= 0 && curr_x - 1 >= 0)
    if (grid[curr_y][curr_x] == "X" && grid[curr_y - 1][curr_x - 1] == "M" && grid[curr_y - 2][curr_x - 2] == "A" && grid[curr_y - 3][curr_x - 3] == "S")
      count += 1
    end
  end

  if (curr_y + 3 < row_n && curr_y + 2 < row_n && curr_y + 1 < row_n && curr_x - 3 >= 0 && curr_x - 2 >= 0 && curr_x - 1 >= 0)
    if (grid[curr_y][curr_x] == "X" && grid[curr_y + 1][curr_x - 1] == "M" && grid[curr_y + 2][curr_x - 2] == "A" && grid[curr_y + 3][curr_x - 3] == "S")
      count += 1
    end
  end
  
  if (curr_y - 3 >= 0 && curr_y - 1 >= 0 && curr_y - 1 >= 0 && curr_x + 3 < col_n && curr_x + 2 < col_n && curr_x + 1 < col_n)
    if (grid[curr_y][curr_x] == "X" && grid[curr_y - 1][curr_x + 1] == "M" && grid[curr_y - 2][curr_x + 2] == "A" && grid[curr_y - 3][curr_x + 3] == "S")
      count += 1
    end
  end
  
  return count
end

ans = 0
grid.each_with_index do |row, y|
  row.each_with_index do |char, x|
    c = check(y, x, grid)
    ans += c
  end
end

puts ans