from itertools import permutations
A = list(map(int, input().split()))
ans = 10**5
for a in permutations(A):
    ans = min(ans, abs(a[1] - a[0]) + abs(a[2] - a[1]))
print(ans)
