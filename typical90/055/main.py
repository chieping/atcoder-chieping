from itertools import combinations
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for c in combinations(A, 5):
    if c[0]*c[1]%P*c[2]%P*c[3]%P*c[4]%P == Q:
        ans += 1
print(ans)
