from pprint import pprint as pp
import copy

with open('input.txt') as f:
  lines = [x.strip() for x in f.readlines()]

visited = set()

grid = [[' '] * 6 for i in range(5)]

H = [1000, 1000]
T = [[1000, 1000] for _ in range(9)]


def check_dirs(i, state):
  # R
  if T[i][1] + 2 == T[i - 1][1]:
    T[i][1] += 1

    if T[i][0] - 2 == T[i - 1][0]:
      T[i][0] -= 1
    elif T[i][0] + 2 == T[i - 1][0]:
      T[i][0] += 1
    else:
      T[i][0] = T[i - 1][0]
  # L
  elif T[i][1] - 2 == T[i - 1][1]:
    T[i][1] -= 1

    if T[i][0] - 2 == T[i - 1][0]:
      T[i][0] -= 1
    elif T[i][0] + 2 == T[i - 1][0]:
      T[i][0] += 1
    else:
      T[i][0] = T[i - 1][0]
  # U
  elif T[i][0] - 2 == T[i - 1][0]:
    T[i][0] -= 1

    if T[i][1] + 2 == T[i - 1][1]:
      T[i][1] += 1
    elif T[i][1] - 2 == T[i - 1][1]:
      T[i][1] -= 1
    else:
      T[i][1] = T[i - 1][1]
  # D
  elif T[i][0] + 2 == T[i - 1][0]:
    T[i][0] += 1

    if T[i][1] + 2 == T[i - 1][1]:
      T[i][1] += 1
    elif T[i][1] - 2 == T[i - 1][1]:
      T[i][1] -= 1
    else:
      T[i][1] = T[i - 1][1]


for line in lines:
  dir, dist = line.split()

  for _ in range(int(dist)):
    state = copy.deepcopy(T)
    if dir == 'R':
      H[1] += 1

      prev = T[0]

      if T[0][1] + 2 == H[1]:
        T[0][1] = H[1] - 1
        T[0][0] = H[0]

      for i in range(1, len(T)):
        check_dirs(i, state)
    elif dir == 'L':
      H[1] -= 1

      if T[0][1] - 2 == H[1]:
        T[0][1] = H[1] + 1
        T[0][0] = H[0]

      for i in range(1, len(T)):
        check_dirs(i, state)
    elif dir == 'U':
      H[0] -= 1

      if T[0][0] - 2 == H[0]:
        T[0][0] = H[0] + 1
        T[0][1] = H[1]

      for i in range(1, len(T)):
        check_dirs(i, state)
    else:
      H[0] += 1

      if T[0][0] + 2 == H[0]:
        T[0][0] = H[0] - 1
        T[0][1] = H[1]

      for i in range(1, len(T)):
        check_dirs(i, state)

    # for i in reversed(range(len(T))):
    #   # print(T[i][0], T[i][1])
    #   grid[T[i][0]][T[i][1]] = str(i+1)
    # grid[H[0]][H[1]] = 'H'
    # pp(grid)
    # grid = [[' '] * 6 for _ in range(5)]

    visited.add((T[-1][0], T[-1][1]))

print(len(visited))
