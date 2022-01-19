import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
ans = 0
max_ = 0
for a in A:
    max_ = max(max_, a)
    ans += max_ - a
print(ans)
