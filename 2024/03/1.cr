input = File.read("input.txt")

ans = 0

re = /mul\(\d{1,3},\d{1,3}\)/

matches = [] of String
input.scan(re) do |match|
  matches << match[0]
end

matches.each do |match|
  match = match.sub("mul(") { "" }
  match = match.sub(")") { "" }
  n = match.split(',')[0].to_i
  m = match.split(',')[1].to_i
  ans += n * m
end

puts ans

# (wrong)
# 147944979
# 183177929
# 133216444
# 59719593
# 49238633
# 107069718
# 162693101