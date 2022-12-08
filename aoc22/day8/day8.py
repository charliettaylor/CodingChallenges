with open('input.txt') as f:
  lines = [x.strip() for x in f.readlines()]

grid = []

for line in lines:
  numbered = [int(x) for x in line]
  grid.append(numbered)

coords = set()
# columns skip first and last cuz vis
for i in range(1, len(grid) - 1):
  max = grid[i][0]
  for j in range(1, len(grid[i]) - 1):
    if grid[i][j] > max:
      coords.add((i, j))
      max = grid[i][j]

for i in reversed(range(1, len(grid) - 1)):
  max = grid[i][-1]
  for j in reversed(range(1, len(grid[i]) - 1)):
    if grid[i][j] > max:
      coords.add((i, j))
      max = grid[i][j]

for i in range(1, len(grid[0]) - 1):
  max = grid[0][i]
  for j in range(1, len(grid) - 1):
    if grid[j][i] > max:
      coords.add((j, i))
      max = grid[j][i]

for i in reversed(range(1, len(grid[0]) - 1)):
  max = grid[-1][i]
  for j in reversed(range(1, len(grid) - 1)):
    if grid[j][i] > max:
      coords.add((j, i))
      max = grid[j][i]

outside = (len(grid) * 2) + (len(grid[0]) - 2) * 2


print(len(coords) + outside)