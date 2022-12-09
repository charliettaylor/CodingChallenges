with open('input.txt') as file:
  lines = [line.rstrip().lower() for line in file]

values = {
    'a': 1,
    'b': 2,
    'c': 3
}

points = 0

for line in lines:
  opp, end = line.split()

  if end == 'x':
    points += (3 if values[opp] == 1 else values[opp] - 1)
  elif end == 'y':
    points += 3 + values[opp]
  else:
    points += 6 + (1 if values[opp] == 3 else values[opp] + 1)

print(points)
