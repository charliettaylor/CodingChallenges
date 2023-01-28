# N and M
start = [int(x) for x in input().split()]

while True:
  first = []
  second = []
  m = start[1]
  n = start[0]
  i = 0

  rng = False
  last = -1
  for i in range(n):
    num = int(input())
    
    if rng and last + 1 != num:
      first.append((last, num))
      rng = False
    elif rng and last + 1 == num:
      continue
    else:
      rng = True
      last = num
  
  rng = False
  last = -1
  prev = -1
  for i in range(m):
    num = int(input())
    print('last', last, 'prev', prev, 'num', num, 'rng', rng)
    if rng and prev + 1 != num:
      second.append((last, prev))
      rng = False
    elif rng and prev + 1 == num:
      prev = num
      continue
    else:
      rng = True
      last = num
      prev = num
  
  

  print(first)
  print(second)

  start = [int(x) for x in input().split()]

  if sum(start) == 0:
    break
