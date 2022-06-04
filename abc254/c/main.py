N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [(a, i) for i, a in enumerate(A)]
B.sort()
prev = -1
for j in range(N):
    a, i = B[j]
    if a == prev:
        continue
    if (i-j) % K != 0:
        C = []
        k = 0
        while j+k < N and B[j+k][0] == a:
            C.append(B[j+k][1])
            k += 1
        if list(sorted(m % K for m in range(j, j+k))) != list(sorted([c % K for c in C])):
            print('No')
            exit()
    prev = a

print('Yes')