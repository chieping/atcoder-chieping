n = int(input())
P = list(map(int, input().split()))

idx1 = P.index(1)
rev = True
if P[(idx1+1)%n] == 2:
    rev = False

if n == 1:
    ans = 0
elif n == 2:
    if P[0] == 1:
        ans = 0
    else:
        ans = 1
else:
    if rev:
        ans = min(idx1+2, n-idx1)
    else:
        ans = min(idx1, n-idx1+2)
print(ans)
