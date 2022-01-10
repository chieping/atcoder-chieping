import sys
readline = sys.stdin.readline
N = int(readline())
ans = 0
for _ in range(N):
    a, b = map(int, readline().split())
    ans += (b+a)*(b-a+1)//2
print(ans)
