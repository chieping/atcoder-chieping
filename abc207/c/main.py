N = int(input())

ARY = []

for i in range(N):
    t, l, r = map(int, input().split())

    if t == 1:
        ARY.append([l, r])
    elif t == 2:
        ARY.append([l, r - 0.1])
    elif t == 3:
        ARY.append([l + 0.1, r])
    elif t == 4:
        ARY.append([l + 0.1, r - 0.1])

ans = 0

for i, lr in enumerate(ARY[:-1]):

    l, r = lr

    for j in range(i + 1, len(ARY)):

        L, R = ARY[j]

        if not(R < l or r < L):
            ans += 1

print(ans)
