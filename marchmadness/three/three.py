iw, ih = [int(x) for x in input().split()]

ins = []

for i in range(ih):
  ins.append(input())

mem = []

mw, mh = [int(x) for x in input().split()]

for _ in range(mh):
  mem.append(input())

for i in range(len(mem)):
  for j in range(len(mem[i])):
    if mem[i][j:j+iw] == ins[0]:
      mem[i] = mem[i][:j] + mem[i][j+1:]
      break

