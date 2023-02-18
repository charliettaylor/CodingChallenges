year = int(input())

start = [4,2018]

compute = [2018]

for x in range(5000):
  start[0] += 2
  start[1] += 2
  if start[0] > 12:
    start[0] %= 12
    start[1] += 1

  compute.append(start[1])

if year in compute:
  print("yes")
else:
  print("no")