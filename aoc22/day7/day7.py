with open('input.txt') as f:
  lines = f.readlines()

directory = dict()
folders = dict()
folderLinks = dict()
currdir = []
nextIsInput = False
allFiles = set()

def process_cmd(currdir, line: str):
  last = line.split()[-1]
  if line.startswith('cd') and last != '/' and last != '..':
    currdir.append(last)
  elif last == '..':
    currdir.pop(-1)
  return currdir


def process_output(currdir, line: str):
  fir, sec = line.split()

  if fir.isdigit():
    return (int(fir), sec)
  else:
    path = '/'.join(currdir)
    if path in folderLinks:
      folderLinks[path] += sec
    else:
      folderLinks[path] = [sec]


for line in lines:
  nextIsInput = not line.startswith('$')
  if nextIsInput:
    out = process_output(currdir, line)
    check = directory.get('/'.join(currdir))

    if out is None:
      continue

    currpath = f"{'/'.join(currdir)}/{out[-1]}"
    if currpath not in directory:
      directory[currpath] = out[0]
      continue

    if not currpath in allFiles:
      directory[currpath] += out[0]
      allFiles.add(currpath)

    if currdir[-1] in folders:
      folders[currdir[-1]] += out[0]
    else:
      folders[currdir[-1]] = out[0]
  else:
    currdir = process_cmd(currdir, line[2:])

print(directory)

print(folders)