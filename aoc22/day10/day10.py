with open('input.txt') as f:
  lines = f.readlines()

cycles = 0
reg = 1
total = 0

for line in lines:
  if line.startswith('add'):
    thing, num = line.split()
    for i in range(2):  
      cycles += 1
      if cycles in [20, 60, 100, 140, 180, 220]:
        total += reg * cycles
    reg += int(num)
  else:
    cycles += 1
    if cycles in [20, 60, 100, 140, 180, 220]:
      total += reg * cycles
  
  
print(total)