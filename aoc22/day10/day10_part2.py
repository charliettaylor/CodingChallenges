with open('input.txt') as f:
  lines = f.readlines()

cycles = 0
reg = 1
total = 0

output = []

for line in lines:
  if line.startswith('add'):
    thing, num = line.split()
    for i in range(2):  
      if cycles % 40 in range(reg-1, reg+2):
        print('#', end='')
      else:
        print('.', end='')

      cycles += 1

      if cycles % 40 == 0:
        print()
    reg += int(num)
  else:
    if cycles % 40 in range(reg-1, reg+2):
      print('#', end='')
    else:
      print('.', end='')
    
    cycles += 1
    if cycles % 40 == 0:
      print()
