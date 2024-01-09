from pprint import pprint as pp
from dataclasses import dataclass
from collections import Counter

@dataclass
class Hand:
    cards: str
    bet: int
    typeh: int

def swap(hands, i, j):
    temp = hands[i]
    hands[i] = hands[j]
    hands[j] = temp

prio = "AKQJT98765432"

with open('in.txt') as f:
    lines = f.readlines()

hands = []

for line in lines:
    cards, bet = line.split()
    hands.append(Hand(cards, bet, 0))

for hand in hands:
    count = Counter(hand.cards)
    values = count.values()
    pp(count)
    
    if 5 in values:
        hand.typeh = 6 
    elif 4 in values:
        hand.typeh = 5
    elif 3 in values:
        if 2 in count.values():
            hand.typeh = 4
        else:
            hand.typeh = 3
    elif 2 in values:
        if list(values).count(2) > 1:
            hand.typeh = 2
        else:
            hand.typeh = 1
    else:
        hand.typeh = 0

for i in range(len(hands)):
    for j in range (1, len(hands)):
        left, right = hands[i].typeh, hands[j].typeh
        
        if left < right:
            swap(hands, i, j)
        elif left == right:
            for k in range(5):
                l, r = hands[i].cards[k], hands[j].cards[k]
                if prio.find(l) > prio.find(r):
                    swap(hands, i, j)
                    break

pp(hands)