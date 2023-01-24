from itertools import product
from dataclasses import dataclass
from collections import OrderedDict
from pprint import pprint as pp

@dataclass
class Stats:
  damage: int
  defense: int
  stars: int

@dataclass
class Result:
  dTaken: int
  stars: int

perms = [''.join(p) for p in product('ads', repeat=4)]
copy = [''.join(sorted(x)) for x in perms]
uq = []
while copy:
  uq.append(copy[0])
  copy = [x for x in copy if x != copy[0]]

perms = uq

d = dict()
winDict = OrderedDict()

for perm in perms:
  d[perm] = Stats(perm.count('a') * 2, perm.count('d'), perm.count('s'))

for p1 in perms:
  wins = 0
  for p2 in perms:
    if p1 == p2:
      continue
    
    p1DamageTaken = max(d[p2].damage - (d[p1].defense * 2), 0)
    p2DamageTaken = max(d[p1].damage - (d[p2].defense * 2), 0)

    p1DefDamage = min(d[p1].damage // 2, d[p2].defense)
    p2DefDamage = min(d[p2].damage // 2, d[p1].defense)

    p1Result = Result(p1DamageTaken + p1DefDamage, d[p1].stars - d[p2].stars)
    p2Result = Result(p2DamageTaken + p2DefDamage, d[p2].stars - d[p1].stars)

    if p1Result.stars == 3 or p1Result.dTaken < p2Result.dTaken:
      wins += 1
  winDict[p1] = wins

pp(sorted(winDict.items(), key=lambda x: x[1]))
# pp(sorted(winDict))
