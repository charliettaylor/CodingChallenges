import math

with open("in.txt") as f:
    lines = f.readlines()

time = []
dist = []

time = lines[0].split(":")[-1]
dist = lines[1].split(":")[-1]
time = [int(x.strip()) for x in time.split()]
dist = [int(x.strip()) for x in dist.split()]

print(time, dist)

# d = r * t

ways = []

for i in range(len(time)):
    t, d = time[i], dist[i]
    traveled = []
    for slice in range(t):
        rate = slice
        time_left = t - slice
        traveled.append(rate * time_left)

    ways.append(len([x for x in traveled if x > d]))

print(math.prod(ways))
