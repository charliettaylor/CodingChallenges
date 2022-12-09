with open('input.txt') as file:
  lines = [line.rstrip().lower() for line in file]

match = {
    'a': 'x',
    'b': 'y',
    'c': 'z'
}

values = {
    'x': 1,
    'y': 2,
    'z': 3
}

points = 0

for line in lines:
  opp, me = line.split()

  oppMap = match[opp]

  if oppMap == me:
    points += 3 + values[me]
  elif values[me] == values[oppMap] + 1 or values[oppMap] == values[me] + 2:
    points += 6 + values[me]
  else:
    points += values[me]

print(points)
