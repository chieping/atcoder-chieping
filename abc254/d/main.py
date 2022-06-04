N = int(input())


ans = 0

for i in range(1, N+1):
    h = i * i

    a = []

    # 約数列挙
    j = 2
    while j <= N:
        d, r = divmod(h, j)
        if r == 0:
            a.append(j)
            h = d
        j += 1
    print(a)
    ans += len(a) + 1
        



print(ans)