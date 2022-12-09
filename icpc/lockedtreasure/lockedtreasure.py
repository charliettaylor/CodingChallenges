import math

cases = int(input())
for i in range(cases):
  l, r = input().split()
  print(str(math.comb(int(l), int(r) - 1)))
