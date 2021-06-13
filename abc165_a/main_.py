m = int(input())
min, max = map(int, input().split())

ans = "NG"

for i in range(min, max + 1):
    if i % m == 0:
        ans = "OK"
        break

print(ans)
