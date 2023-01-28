# with open('input.txt') as f:
#   line = f.readline().strip()
import string

line = input()
def isValid(word: str):
  for char in word:
    if (char != 'u' and char != 'm') and (char not in string.punctuation):
      return False

  return True

words = line.split()

parsed = ''

for word in words:
  if not isValid(word):
    continue

  for punc in string.punctuation:
    word = word.replace(punc, '')

  parsed += word.replace('u', '1').replace('m', '0')

final = ''
for i in range(0, len(parsed), 7):
  curr = parsed[i:i+7]
  num = chr(int(curr, 2))
  
  final += num

print(final)