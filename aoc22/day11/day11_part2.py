from dataclasses import dataclass
from math import floor
from pprint import pprint as pp

@dataclass
class Monkey:
  id: int
  items: list[int]
  operation: str
  op_val: int
  test: int
  true_move: int
  false_move: int
  inspect: int


with open('input.txt') as f:
  lines = [x.strip() for x in f.readlines()]

i = 0

monkeys: list[Monkey] = []


while i < len(lines):
  id = int(lines[i][-2])
  items = [int(x) for x in lines[i + 1][16:].split(', ')]
  ops = lines[i + 2][17:].split()
  op = ops[1]
  # 0 is flag for 0ld
  op_val = int(ops[2]) if ops[2] != 'old' else 0
  test = int(lines[i + 3].split()[-1])
  true_move = int(lines[i + 4].split()[-1])
  false_move = int(lines[i + 5].split()[-1])

  monkeys.append(Monkey(id, items, op, op_val, test, true_move, false_move, 0))
  i += 7

# Chinese Remainder Theorem FTW(?) 😢🐒
divs = [x.test for x in monkeys]
crt = 1
for x in divs:
  crt *= x

for r in range(10000):
  for m in range(len(monkeys)):
    for i in range(len(monkeys[m].items)):
      curr = monkeys[m]
      op = monkeys[m].op_val if curr.op_val != 0 else curr.items[i]
      
      # apply operation
      if monkeys[m].operation == '+':
        curr.items[i] = (curr.items[i] + op) % crt
      else:
        curr.items[i] = (curr.items[i] * op) % crt
      
      # divide worry by 3
      # curr.items[i] //= 3

      # print(f'after math: {curr.items[i]}, test: {curr.test}, goto: {curr.true_move if curr.items[i] % curr.test == 0 else curr.false_move}')
      # now we test
      if curr.items[i] % curr.test == 0:
        monkeys[curr.true_move].items.append(curr.items[i])
      else:
        monkeys[curr.false_move].items.append(curr.items[i])
    
    monkeys[m].inspect += len(monkeys[m].items)
    monkeys[m].items.clear()
  # if r == 0:
  #   pp(monkeys)
  # print(r)

top2 = sorted([x.inspect for x in monkeys])[-2:]

# pp(monkeys)

print(top2)
print(top2[0] * top2[1])