lines = int(input())

entered = 0
most = 0

departed = ['departed', 'out', 'left', 'exited']

for i in range(lines):
    org = input()
    parts = org.split()
    num = 0
    left = False

    if any([x in departed for x in parts]):
        left = True

    if len(parts) == 2:
      num = 1
    elif parts[0].isnumeric():
        num = int(parts[0])
    elif ',' in org:
        num = org.count(',') + 2
    elif ' and ' in org:
        if parts[2].isnumeric():
            num = int(parts[2]) + 1
        else:
          num = 2
    else:
        num = 1
    
    if left:
        entered -= num
    else:
        entered += num
    
    print(f"{entered=} {num=} {left=}")
    
    most = max(most, entered)

print(most)
        