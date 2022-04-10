from collections import Counter
from pprint import pprint
import sys
input = sys.stdin.readline
N  = int(input())
S = []
T = []
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)
 
SC = Counter(S)
ST = Counter(T)
 
ng = set()
for s, t in zip(S, T):
    if s == t:
        if s in ng:
            print('No')
            exit()
        else:
            ng.add(s)
            continue
 
    if SC[s] + ST[s] == 1 or SC[t] + ST[t] == 1:
        if s in ng or t in ng:
            print('No')
            exit()
        else:
            continue
        
    if SC[s] + ST[s] > 1 and SC[t] + ST[t] > 1:
        print('No')
        exit()
    if SC[s] + ST[s] > 1:
        if t not in ng:
            ng.add(t)
            continue
        else:
            print('No')
            exit()
    if SC[t] + ST[t] > 1:
        if s not in ng:
            ng.add(s)
            continue
        else:
            print('No')
            exit()
 
print('Yes')