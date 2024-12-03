line = File.read("input.txt")

ans = 0

re = /mul\(\d{1,3},\d{1,3}\)/

re2 = /(?<=don't\(\))(.*?)(?=do\(\))/

re3 = /(?<=don't\(\))(.*?)(?=do\(\))/

clean = ""
# lines.each_with_index do |line, i|
temp = line
line.scan(re3) do |match|
  puts match
  temp = line.sub(match[0]) {""}
  clean += temp
end
# end

# matches = [] of String
# clean.scan(re) do |match|
#   matches << match[0]
# end
# # puts matches

# matches.each do |match|
#   match = match.sub("mul(") { "" }
#   match = match.sub(")") { "" }
#   n = match.split(',')[0].to_i
#   m = match.split(',')[1].to_i
#   # ans += n * m
# end

# # puts clean

# puts matches
# #
