from math import prod


def mins(pull_list: str) -> dict:
    curr = {"red": 0, "blue": 0, "green": 0}
    mins = {"red": 0, "blue": 0, "green": 0}

    for pulls in pull_list.split(";"):
        for block in [x.strip() for x in pulls.split(",")]:
            qty, color = block.split()
            qty = int(qty)

            curr[color] = qty

        for color in curr:
            mins[color] = max(mins[color], curr[color])

        curr.clear()

    return mins


with open("in2.txt") as f:
    lines = f.readlines()

sum = 0
print(lines)
for line in lines:
    name, game = line.split(":")
    name = int(name.split()[-1])

    sum += prod(mins(game).values())

print(sum)
