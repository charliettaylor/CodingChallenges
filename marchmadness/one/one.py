lines = int(input())

entered = set()
most = 0

for i in range(lines):
    name, left = input().split()[:2]
    left = left == 'left'

    if name not in entered and not left:
        entered.add(name)
      
    if name in entered and left:
        entered.remove(name)
    
    most = max(most, len(entered))


print(most)