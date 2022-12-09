with open('input.txt') as f:
  lines = f.readlines()

curdir = ''
path = ['']
dirSizes = {}
fileNames = set()

for line in lines:
  if line.startswith('$'):
    chunks = line.split()
    if 'cd' in chunks and '..' not in chunks and chunks[-1] != '/':
      # print(chunks)
      # update current dir and path
      path.append(chunks[-1])
      print(path)
      curdir = chunks[-1]
    elif '..' in chunks:
      path.pop()
      curdir = path[-1]
  else:
    chunks = line.split()
    if chunks[0].isdigit():
      subPath = [x for x in path]
      if chunks[1] in fileNames:
        continue
      fileNames.add(f'{"/".join(subPath)}/{chunks[1]}')
      while len(subPath) > 1:
        curr = '/'.join(subPath)
        if curr not in dirSizes:
          dirSizes[curr] = int(chunks[0])
        else:
          dirSizes[curr] += int(chunks[0])
        subPath.pop()

cumsum = 0

for val in dirSizes.values():
  if val <= 100000:
    cumsum += val

# print(dirSizes)
print('cum', cumsum)
