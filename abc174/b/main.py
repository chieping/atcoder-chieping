import sys
readline = sys.stdin.readline
N, D = map(int, readline().split())
ans = 0
for _ in range(N):
    x, y = map(int, readline().split())
    ans += D*D >= x*x + y*y
print(ans)    
