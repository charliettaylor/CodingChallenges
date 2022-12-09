from pprint import pprint as pp

with open('input.txt') as f:
  lines = [x.strip() for x in f.readlines()]

visited = set()
grid = [[' '] * 6 for i in range(5)]

H = [1000, 1000]
T = [1000, 1000]

pp(grid)

for line in lines:
  dir, dist = line.split()

  for i in range(int(dist)):
    if dir == 'R':
      H[1] += 1
      if T[1] + 2 == H[1]:
        T[1] = H[1] - 1
        T[0] = H[0]
    elif dir == 'L':
      H[1] -= 1
      if T[1] - 2 == H[1]:
        T[1] = H[1] + 1
        T[0] = H[0]
    elif dir == 'U':
      H[0] -= 1
      if T[0] - 2 == H[0]:
        T[0] = H[0] + 1
        T[1] = H[1]
    else:
      H[0] += 1
      if T[0] + 2 == H[0]:
        T[0] = H[0] - 1
        T[1] = H[1]
    print(T)
    visited.add((T[0], T[1]))

    # grid[H[0]][H[1]] = 'H'
    # grid[T[0]][T[1]] = 'T'
    # pp(grid)
    # grid = [[' '] * 6 for _ in range(5)]


print(len(visited) - 1)
