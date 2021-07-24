n = int(input())
a = sorted(list(map(int, input().split())))[::-1]

ans = 0
for i in range(0, n-2):
    if a[i] <= a[i+1] + a[i+2]:
        ans = a[i] + a[i+1] + a[i+2]
        break

print(ans)
