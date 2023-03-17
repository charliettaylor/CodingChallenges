from math import pi

n = int(input())

pis = []



for i in range(n):
    r, a = input().split()
    r = int(r)
    a = float(a)

    # a = pi * r^2

    prox = a / (r ** 2)
    pis.append((i, abs(pi - prox), r))

sortedP = sorted(pis, key=lambda x: x[1])

prod = 1
for i in range(min(5, len(pis))):
    prod *= pis[sortedP[i][0]][2]

print(prod)