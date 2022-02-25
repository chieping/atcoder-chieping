A, B = map(int, input().split())
ans = 0
now = 1
while now < B:
    now -= 1
    now += A
    ans += 1
print(ans)