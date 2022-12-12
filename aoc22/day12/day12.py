from pprint import pprint as pp

with open('input.txt') as f:
  lines = [x.strip() for x in f.readlines()]

# S is start
grid = []
adj = {}

S = ()
E = ()

for i, line in enumerate(lines):
  temp = []
  for j, x in enumerate(line):
    if x == 'E':
      E = (i, j)
      temp.append(26)
    elif x == 'S':
      S = (i,j)
      temp.append(1)
    else:
      temp.append(ord(x) - 96)
  grid.append(temp)

# pp(grid)
# print(S, E)

for row in range(len(grid)):
  for col in range(len(grid[row])):
    adj[(row, col)] = []

    for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
      try:
        if row + dir[0] < 0 or col + dir[1] < 0:
          continue

        next = grid[row + dir[0]][col + dir[1]]
        if grid[row][col] - next in range(-1,2):
          adj[(row, col)].append((row + dir[0], col + dir[1]))
      except:
        pass
    
# pp(adj)

# visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  
  while queue:
    s = queue.pop(0)
    print(s)
    if s == E:
      print(f'DONE! {len(visited)}')
    for n in graph[s]:
      # if n not in visited:
        visited.append(n)
        queue.append(n)

bfs([], adj, (0,0))