K = int(input())
F = []

for i in range(1, K):
    if i**2 > K:
        break
    if K % i != 0:
        continue
    F.append(i)
    if (i != K // i):
        F.append(K // i)

F.sort()
ans = 0
for i in range(len(F)):
    for j in range(i, len(F)):
        a = F[i]
        b = F[j]
        c = 0
        if (K // a) < b:
            continue
        if K % (a*b):
            continue
        c = K // (F[i]*F[j])
        if b <= c:
            ans += 1
print(ans)
