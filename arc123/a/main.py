A = list(map(int, input().split()))

d1 = A[1] - A[0]
d2 = A[2] - A[1]

ans = 0

if d1 < d2:
    p = abs(d2 - d1) // 2
    if abs(d2 - d1) % 2 == 1:
        p += 1
    ans += p
    d1 += p
    d2 -= p

if d1 != d2:
    ans += abs(d2 - d1)

print(ans)

# if d1 > d2:
#     p = abs(d1 - d2)
#     d1 -= p
#     ans += p

# if d2 > d1:
#     p = abs(d2 - d1)
#     d2 -= p
#     ans += p

# print(ans)

