from itertools import accumulate
import sys
input = sys.stdin.readline
Q = int(input())
LR = []
for _ in range(Q):
    LR.append(tuple(map(int, input().split())))
Max = 10**5+10

prime = [True] * Max
prime[1] = False

i = 2
while i*i < Max:
    if prime[i]:
        j = i+i
        while j < Max:
            prime[j] = False
            j += i
    i += 1

# print(*[i for i in range(1, 101) if prime[i]])
res = [0] * Max
for i in range(1, Max, 2):
    res[i] = prime[i] and prime[(i+1)//2]
cum = list(accumulate(res))

for l, r in LR:
    print(cum[r] - cum[l-1])
