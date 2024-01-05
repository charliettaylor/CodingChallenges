RED = 12
GREEN = 13
BLUE = 14


def valid_game(pull_list: str) -> bool:
    for pulls in pull_list.split(";"):
        for block in [x.strip() for x in pulls.split(",")]:
            qty, color = block.split()
            qty = int(qty)
            if (
                ("red" == color and qty > RED)
                or ("blue" == color and qty > BLUE)
                or ("green" == color and qty > GREEN)
            ):
                return False

    return True


with open("in.txt") as f:
    lines = f.readlines()
sum = 0
for line in lines:
    name, game = line.split(":")
    name = int(name.split()[-1])

    if valid_game(game):
        sum += name

print(sum)
