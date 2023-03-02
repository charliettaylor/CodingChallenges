def solve():
  h,w,n = [int(x) for x in input().split()]
  bricks = [int(x) for x in input().split()]
  layer = 0
  height = 1
  for b in bricks:
      layer += b
      if layer > w:
          return 'NO'
      if layer == w:
          layer = 0
          height += 1

  if height >= h:
    return "YES"

  return "NO"

print(solve())