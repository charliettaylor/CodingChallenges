cases = int(input())
people = []

for _ in range(cases):
  people.append(input().strip().split())

# name, start, birth, courses

for p in people:
  if int(p[1][:4]) >= 2010:
    print(f"{p[0]} eligible")
  elif int(p[2][:4]) >= 1991:
    print(f"{p[0]} eligible")
  elif int(p[-1]) < 41:
    print(f"{p[0]} coach petitions")
  else:
    print(f"{p[0]} ineligible")