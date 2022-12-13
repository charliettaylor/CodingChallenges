import ast
from pprint import pprint as pp

with open('input.txt') as f:
  lines = [x.strip() for x in f.readlines()]

pairs = []

for i in range(0, len(lines), 3):
  first = lines[i]
  second = lines[i+1]
  pairs.append((ast.literal_eval(first), ast.literal_eval(second)))

def compare(one: list, two: list) -> bool:
  while len(one) and len(two):
    # print(one, two)
    
    if len(two) == 0 and len(one) != 0:
      return False
    
    if len(two) != 0 and len(one) == 0:
      return True
    
    if type(one[0]) is not list and type(two[0]) is not list:
      if one[0] > two[0]:
        return False
    else:
      lone = list(one[0] if type(one[0]) is list else [one[0]])
      ltwo = list(two[0] if type(two[0]) is list else [two[0]])
      return compare(lone, ltwo)

    one.pop(0)
    two.pop(0)


  if len(two) == 0 and len(one) != 0:
    return False
  return True

count = 0
for i, (one, two) in enumerate(pairs):
  if compare(one, two):
    print(i + 1)
    count += (i + 1)
  
print(count)