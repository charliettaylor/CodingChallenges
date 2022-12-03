with open('input.txt') as file:
  lines = [line.rstrip() for line in file]

maxList = []

for line in lines:
  first, second = line[:len(line) // 2], line[len(line) // 2:]
  for i in first:
    curr = ord(i)
    if i in second:
      maxList.append(curr - 96 if curr >= 97 else curr - 65 + 27)
      break

final = 0

for i in maxList:
  final += i

print(final)