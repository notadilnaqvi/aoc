lines = File.read_lines("input.txt")

ans = 0

re = /mul\(\d{1,3},\d{1,3}\)/

re2 = /don't\(\).+?do\(\)/

lines.each_with_index do |input, _|
  matches = [] of String
  input_clean = input
  input.scan(re2) do |match|
    input_clean = input_clean.sub(match[0], "")
    input_clean.scan(re) do |match|
      matches << match[0]
    end
  end
  
  matches.each do |match|
    match = match.sub("mul(") { "" } 
    match = match.sub(")") { "" }
    n = match.split(',')[0].to_i
    m = match.split(',')[1].to_i
    ans += n * m
  end
end

puts ans

# 74962554 nope