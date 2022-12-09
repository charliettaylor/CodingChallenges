with open('input.txt') as f:
  lines = f.readlines()

curdir = ''
path = ['']
dirSizes = {}

for line in lines:
  if line.startswith('$'):
    chunks = line.split()
    if 'cd' in chunks and '..' not in chunks and chunks[-1] != '/':
      path.append(chunks[-1])
      curdir = chunks[-1]
    elif '..' in chunks:
      path.pop()
      curdir = path[-1]
  else:
    chunks = line.split()
    if chunks[0].isdigit():
      subPath = [x for x in path]
      while len(subPath):
        curr = '/'.join(subPath)
        if curr not in dirSizes:
          dirSizes[curr] = int(chunks[0])
        else:
          dirSizes[curr] += int(chunks[0])
        subPath.pop()


max = 70_000_000
need = 30_000_000
cumsum = dirSizes['']

left = max - cumsum

diff = need - left

min = 1000000000000000000000
name = ''

for size in dirSizes.values():
  if size < min and size > diff:
    min = size

print(min)
