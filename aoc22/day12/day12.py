from pprint import pprint as pp

with open('input.txt') as f:
  lines = [x.strip() for x in f.readlines()]

class Node:
  def __init__(self, pos, height) -> None:
    self.pos = pos
    self.height = height
    self.path = []

# S is start
grid = []

S = Node((0,0), -1)
E = Node((0,0), -1)

for i, line in enumerate(lines):
  temp = []
  for j, x in enumerate(line):
    if x == 'E':
      E = Node((i, j), 1)
      temp.append(26)
    elif x == 'S':
      S = Node((i,j), 26)
      temp.append(1)
    else:
      temp.append(ord(x) - 96)
  grid.append(temp)

pp(grid)
print(S, E)
# for dir in [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(start):
  queue: list[Node] = [start]
  visited = set([start])

  while len(queue):
    curr = queue.pop(0)
    if curr.pos == E.pos:
      print(f"DONE {len(curr.path)}")
      return len(curr.path)
    
    for r, c in [[1,0],[-1,0],[0,1],[0,-1]]:
      n = (curr.pos[0] + r, curr.pos[1] + c)
      if n[0] < 0 or n[0] > len(grid[0]) or n[1] < 0 or n[1] > len(grid):
        continue

      next = grid[n[0]][n[1]]
      if next - curr.height > 1 or curr in visited:
        continue

      node = Node(curr, next)
      node.path = curr.path[:]
      node.path.append(curr)
      visited.append(curr)
      queue.append(node)
  return 1_000_000_000

print(bfs(S))
