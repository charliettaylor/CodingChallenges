import math

rooms = input()

rooms = []

for _ in range(rooms):
  rooms.append(input())

graph = {}

for room in rooms:
  graph[room] = set()
  for other in rooms:
    if other == room:
      continue

    gcd = math.gcd(room, other)
    if gcd > 1:
      graph[room].add((other, gcd))


# to be continued...
