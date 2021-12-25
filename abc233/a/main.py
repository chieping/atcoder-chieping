X, Y = map(int, input().split())
ans = 0
while (X + ans*10) < Y:
    ans += 1
print(ans)
