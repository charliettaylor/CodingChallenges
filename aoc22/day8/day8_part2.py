with open('input.txt') as f:
  lines = [x.strip() for x in f.readlines()]

grid = []

for line in lines:
  numbered = [int(x) for x in line]
  grid.append(numbered)


score = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    curr = grid[i][j]
    # from curr to top
    scores = [0, 0, 0, 0]
    for k in reversed(range(i)):
      if grid[k][j] < curr:
        scores[0] += 1
      else:
        scores[0] += 1
        break

    # from curr to bottom
    for k in range(i + 1, len(grid)):
      if grid[k][j] < curr:
        scores[1] += 1
      else:
        scores[1] += 1
        break

    # from curr to left
    for k in reversed(range(j)):
      if grid[i][k] < curr:
        scores[2] += 1
      else:
        scores[2] += 1
        break

    # from curr to right
    for k in range(j + 1, len(grid[0])):
      if grid[i][k] < curr:
        scores[3] += 1
      else:
        scores[3] += 1
        break

    if i == 0:
      scores[0] -= 1

    if j == 0:
      scores[2] -= 1

    if i == len(grid):
      scores[1] -= 1

    if j == len(grid[0]):
      scores[3] -= 1

    times = scores[0] * scores[1] * scores[2] * scores[3]
    print((i, j), scores)
    # ulrd
    # udlr
    # 0214

    if times > score:
      score = times


# uldr
# 2212
# 1211
print(score)
