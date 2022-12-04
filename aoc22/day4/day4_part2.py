with open('input.txt') as file:
  lines = [line.rstrip() for line in file]

fits = 0

for line in lines:
  first, sec = line.split(',')
  first = [int(x) for x in first.split('-')]
  sec = [int(x) for x in sec.split('-')]

  fRange = range(first[0], first[1] + 1)
  sRange = range(sec[0], sec[1] + 1)

  if first[0] in sRange or first[1] in sRange or sec[0] in fRange or sec[1] in fRange:
    fits += 1

print(str(fits))