from collections import Counter

N = int(input())
cnt = Counter([input() for i in range(N)])

a = 0
ans = ''
for (k, v) in cnt.items():
    if a < v:
        a = v
        ans = k
print(ans)
