# Part 1
import re
with open('input.txt', 'r') as file:
  text = file.read().replace('\n', '')

pattern = r"mul\((-?\d+),(-?\d+)\)"

matches = re.findall(pattern, text)
sum = 0

for x, y in matches:
  sum += int(x)*int(y)

print(sum)

# Part 2
import re
with open('input.txt', 'r') as file:
  raw_text = file.read().replace('\n', '')

do_text = raw_text.split('do()')

for index, t in enumerate(do_text):
  do_text[index] = t.split('don\'t()')[0]

pattern = r"mul\((-?\d+),(-?\d+)\)"

matches = []
for text in do_text:
  if (text == ''): continue
  matches += re.findall(pattern, text)

sum = 0

for x, y in matches:
  sum += int(x)*int(y)

print(sum)