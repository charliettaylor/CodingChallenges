thing = [int(x) for x in input().split()]
one, two = [thing[0], thing[1]], [thing[2], thing[3]]


def score(pair):
  if pair == [1,2] or pair == [2,1]:
    return 1000
  elif pair[0] == pair[1]:
    return 100 * pair[0]
  else:
    return int("".join([str(x) for x in sorted(pair, reverse=True)]))

while one != [0,0]:
  score1, score2 = score(one), score(two)

  if score1 > score2:
    print("Player 1 wins.")
  elif score1 == score2:
    print("Tie.")
  else:
    print("Player 2 wins.")

  thing = [int(x) for x in input().split()]
  one, two = [thing[0], thing[1]], [thing[2], thing[3]]
