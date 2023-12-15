$pretty_map = {
  "F" => "┌",
  "-" => "─",
  "7" => "┐",
  "|" => "│",
  "J" => "┘",
  "L" => "└",
}

def make_pretty(file_path)
  diagram = File.open(file_path).read()
  pretty_diagram = diagram.gsub("F", "┌").gsub("-", "─").gsub("7", "┐").gsub("|", "│").gsub("J", "┘").gsub("L", "└")
  pretty_file_path = file_path.gsub(".txt", ".pretty.txt")
  File.open(pretty_file_path, 'w') { |file| file.write(pretty_diagram) }
end

make_pretty("sample-1.txt")
make_pretty("sample-2.txt")
make_pretty("sample-3.txt")
make_pretty("sample-4.txt")
make_pretty("sample-5.txt")
make_pretty("input.txt")
