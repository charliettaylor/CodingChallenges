from collections import Counter
hand = [x[0] for x in input().split()]
print(Counter(hand).most_common(1)[0][1])