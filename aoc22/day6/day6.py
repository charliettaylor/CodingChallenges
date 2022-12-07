with open('input.txt') as f:
  lines = f.readlines()

mark = ""
answer = 0

for pos, i in enumerate(lines[0]):
  if len(set(lines[0][pos:pos+14])) == len(lines[0][pos:pos+14]):
    print(pos + 14)
    break
