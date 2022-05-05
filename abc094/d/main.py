N = int(input())
A = list(map(int, input().split()))
A.sort()
n = A[-1]
r = 10**10
for a in A:
    if abs(n/2 - a) < abs(n/2 - r):
        r = a
print(n, r)