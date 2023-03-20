b = int(input())
n = int(input())

brackets = []
checks = []

for _ in range(b):
  raw = input()
  strip = raw.replace('$', '').replace('%', '').replace(',', '')

  low, hi, percent = [int(x) for x in strip.split()]

  brackets.append((low, hi, percent / 100))

for _ in range(n):
  p = int(input().replace('$', '').replace(',', ''))
  
  checks.append(p)

checks = [x for x in checks if x > 100]
income = sum(checks)

cur = 0
tax = 0
for lo, hi, percent in brackets:
  if income > hi:
    tax += (hi - lo + 1) * percent
  elif income > lo and income < hi:
    tax += (income - lo + 1) * percent
  else:
    break

print(round(tax))

  
