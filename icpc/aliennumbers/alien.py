lines = int(input())

def alien_to_decimal(src: str, srcLang: str):
  base = len(srcLang)
  total = 0
  for i, digit in enumerate(reversed(src)):
    total += srcLang.find(digit) * (base ** i)
  
  return total


def decimal_to_target(dec: int, targetLang: str):
  base = len(targetLang)
  answer = []
  while dec > 0:
    digit = dec % base
    answer.append(targetLang[digit])
    dec //= base
  
  return ''.join(reversed(answer))


def solve(src, srcLang, targetLang, i):
  srcDec = alien_to_decimal(src, srcLang)
  print(f"Case #{i + 1}: {decimal_to_target(srcDec, targetLang)}")

for i in range(lines):
  src, srcLang, targetLang = [x for x in input().split()]
  solve(src, srcLang, targetLang, i)