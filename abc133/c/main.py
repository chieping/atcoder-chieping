L, R = map(int, input().split())
MOD = 2019
ans = MOD

if R - L >= 2019:
    print(0)
    exit()

for i in range(L, R+1):
    for j in range(i+1, R+1):
        ans = min(ans, i*j%MOD)
        if ans == 0:
            break
print(ans)
