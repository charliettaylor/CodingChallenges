t, s, n = [int(x) for x in input().split()]
bot = s
flips = [int(x) for x in input().split()]

diffs = []

for f in range(1, len(flips)):
  # the amount of sand moved during this period
  diffs.append(flips[f] - flips[f - 1])

ud = False
i = 0
end = 0

while True:
  if ud:
    bot -= 1
    bot = max(bot, 0)
  else:
    bot += 1
    bot = min(bot, s)
  
  i += 1

  if len(flips) == 0 and (bot == 0 or bot == s):
    end = i
    break

  if i in flips:
    ud = not ud
    flips.remove(i)

  # print(bot)

print(max(i - t, 0))