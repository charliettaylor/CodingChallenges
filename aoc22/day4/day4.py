with open('input.txt') as file:
  lines = [line.rstrip() for line in file]

fits = 0

for line in lines:
  first, sec = line.split(',')
  first = [int(x) for x in first.split('-')]
  sec = [int(x) for x in sec.split('-')]

  if (first[0] <= sec[0] <= first[1] and first[0] <= sec[1] <= first[1])\
     or (sec[0] <= first[0] <= sec[1] and sec[0] <= first[1] <= sec[1]):
    fits += 1
    print(line)

print(str(fits))
