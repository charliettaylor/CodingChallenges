with open('input.txt') as file:
  lines = [line.rstrip() for line in file]

elves = []
cumsum = 0

for line in lines:
  if line.isdigit():
    cumsum += int(line)
  else:
    elves.append(cumsum)
    cumsum = 0

print(str(max(elves)))

elves = sorted(elves)
print(int(elves[-1] + elves[-2] + elves[-3]))
