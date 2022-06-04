N, K = map(int, input().split())
A = list(map(int, input().split()))
expected = list(sorted(A))

for i in range(K):
    b = A[i::K]
    b.sort()
    if b != expected[i::K]:
        print('No')
        exit()
print('Yes')