# https://open.kattis.com/problems/everywhere

cases = int(input())

for i in range(cases):
    visitCount = int(input())
    cities = []
    for j in range(visitCount):
      temp = input()
      if temp not in cities:
        cities.append(temp)
    print(len(cities))