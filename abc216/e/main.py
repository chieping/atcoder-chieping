from bisect import bisect_left


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = []
for a in A:
    B.extend(range(1, a+1))
B.sort()

if len(B) <= K:
    print(sum(B))
    exit()

l = 1
r = max(A)
while r - l > 1:
    m = (l + r) // 2

    # Bに含まれるm以上の値の数はK以下か
    if B[-K] >= m:
        l = m
    else:
        r = m

i = bisect_left(B, r)
ans = sum(B[i:])
picked = len(B) - i
ans += (K - picked) * (r-1)

print(ans)
