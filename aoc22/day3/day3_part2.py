with open('input.txt') as file:
  lines = [line.rstrip() for line in file]

maxList = []

for i in range(0, len(lines), 3):
  f, s, t = lines[i], lines[i + 1], lines[i + 2]

  for j in f:
    if j in s and j in t:
      maxList.append(ord(j) - 96 if ord(j) >= 97 else ord(j) - 65 + 27)
      break


final = 0

for i in maxList:
  final += i

print(final)
