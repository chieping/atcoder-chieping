import sys
input = sys.stdin.readline
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[1])
now = 0
ans = True
for a, b in AB:
    now += a
    if now > b:
        ans = False
        break    
print('Yes' if ans else 'No')