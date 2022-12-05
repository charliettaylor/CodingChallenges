with open('input.txt') as f:
  lines = f.readlines()

i = 0
crates = [[], [], [],[], [], [],[], [], []]

while not lines[i][1] == '1':
  curr = 0
  for char in range(1, len(lines[i]), 4):
    if lines[i][char] != ' ':
      crates[curr].append(lines[i][char])
    curr += 1
  i += 1

# print(crates)

for line in lines[i+2:]:
  qty, frm, to = int(line[5:7].strip()), int(line[12:14].strip()), int(line[17:].strip())
  # print(qty, frm, to)
  top = []
  for i in range(qty):
    top = [crates[frm - 1].pop(0)] + top
  crates[to - 1] = list(reversed(top)) + crates[to - 1]
  # print(crates)

print(''.join([x[0] if len(x) > 0 else '' for x in crates]))
