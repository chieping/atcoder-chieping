N = int(input())
P = list(map(int, input().split()))
ans = 0
tmp = 1<<60
for p in P:
    if p <= tmp:
        ans += 1
        tmp = p
print(ans)
