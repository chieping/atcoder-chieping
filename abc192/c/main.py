N, K = input().split()
K = int(K)
N = list(map(int, list(N)))
N.reverse()

for i in range(K):
    if not N:
        print(0)
        exit()
    N.sort()
    g1 = int(''.join(map(str, reversed(N))))
    g2 = int(''.join(map(str, N)))
    f = g1 - g2
    N = []
    while f > 0:
        N.append(f % 10)
        f //= 10
print(*reversed(N), sep='')
