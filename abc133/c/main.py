L, R = map(int, input().split())
MOD = 2019
ans = MOD

for i in range(L, R+1):
    for j in range(i+1, R+1):
        ans = min(ans, i*j%MOD)
        if ans == 0:
            break
    else:
        continue # ここでのcontinueは外側のforでのcontinue
    break
print(ans)
