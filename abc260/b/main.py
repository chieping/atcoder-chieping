N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
used = [False] * N
ABI = list(zip(A, B, range(N)))

ABI.sort(key=lambda x: x[0], reverse=True)
for a, b, i in ABI:
    if X > 0:
        used[i] = True
        X -= 1

ABI.sort(key=lambda x: x[1] * 1000 - x[2], reverse=True)
for a, b, i in ABI:
    if not used[i] and Y > 0:
        used[i] = True
        Y -= 1

ABI.sort(key=lambda x: (x[0] + x[1]) * 1000 - x[2], reverse=True)
for a, b, i in ABI:
    if not used[i] and Z > 0:
        used[i] = True
        Z -= 1

for i, flag in enumerate(used, 1):
    if flag:
        print(i)
