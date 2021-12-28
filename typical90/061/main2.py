from collections import deque
from sys import stdin
Q = int(stdin.readline())
deck = deque()
for _ in range(Q):
    t, x = map(int, stdin.readline().split())
    if t == 1:
        deck.appendleft(x)
    elif t == 2:
        deck.append(x)
    elif t == 3:
        print(deck[x-1])
