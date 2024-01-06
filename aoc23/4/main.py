with open("in.txt") as f:
    lines = f.readlines()

total = 0

for line in lines:
    win, mine = line.split(":")[-1].split("|")
    win = set([int(x.strip()) for x in win.split()])
    mine = set([int(x.strip()) for x in mine.split()])

    inter = win.intersection(mine)

    score = 0
    if len(inter) > 0:
        score = 2 ** (len(inter) - 1)

    total += score


print(total)
