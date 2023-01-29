def main():
  num = int(input())
  lastTwo = num % 100

  if num < 149:
    print("99")
    return
  
  if lastTwo < 49:
    print(str(num - (lastTwo + 1)))
  else:
    print(str(num + (99 - lastTwo)))


if __name__ == "__main__":
  main()
