lines = int(input())

for line in range(lines):
  stuff = [int(x) for x in input().split()][1:]
  avg = round(sum(stuff) / len(stuff), 3)
  total = [x for x in stuff if x > avg]
  percent = (len(total) / len(stuff)) * 100
  print(format(percent, ".3f") + '%')