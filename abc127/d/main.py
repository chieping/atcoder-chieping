import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [tuple(map(int, input().split())) for _ in range(M)]

A.sort()
BC.sort(key=lambda x: x[1], reverse=True)

ans = 0
i = 0
for b, c in BC:
    while b > 0 and i < N:
        if A[i] < c:
            i += 1
            ans += c
            b -= 1
        else:
            break

if i < N:
    ans += sum(A[i:])
print(ans)