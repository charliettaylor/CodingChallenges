length = int(input())

words = []
for _ in range(length):
  words.append(input().strip())

count = 0
wSet = set()
for word in words:
  word = word.lower().replace('-', ' ')
  if word in wSet:
    continue
  count += 1
  wSet.add(word)

print(count)