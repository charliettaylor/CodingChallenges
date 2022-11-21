inp, max = input().split()
max = int(max)
t = 0
values = [int(x) for x in input().split()]

for i in values:
  max -= i
  if max < 0:
    break
  else:
    t += 1

print(t)