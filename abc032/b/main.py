import sys
readline = sys.stdin.readline
s = readline()[:-1]
n = len(s)
k = int(readline())
ans = set()

for l in range(n):
    r = l + k
    if r > n:
        break
    ans.add(s[l:r])

print(len(ans))
