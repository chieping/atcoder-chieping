from sys import stdin
from pprint import pprint
N = list(map(int, stdin.readline()[:-1]))
Nmod3 = list(map(lambda x: x % 3, N))
mod = sum(N) % 3

if mod == 0:
    print(0)
elif mod == 1:
    # 2が2つ or 1が1つ
    if 1 in Nmod3 and len(N) > 1:
        print(1)
    elif Nmod3.count(2) >= 2 and len(N) > 2:
        print(2)
    else:
        print(-1)
elif mod == 2:
    # 2が1つ or 1が2つ
    if 2 in Nmod3 and len(N) > 1:
        print(1)
    elif Nmod3.count(1) >= 2 and len(N) > 2:
        print(2)
    else:
        print(-1)

