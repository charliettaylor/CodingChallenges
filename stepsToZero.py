# 1342. Number of Steps to Reduce a Number to Zero

def numberOfSteps(num: int) -> int:
  count = 0
  while num != 0:
    if num % 2 == 0:
        num //= 2
    else:
        num -= 1

    count += 1

  return count

if __name__ == '__main__':
  print(numberOfSteps(9));