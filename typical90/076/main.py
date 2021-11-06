from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))
target = sum(A) / 10
S = []
S.append(A[0])
for i in range(1, 2*N):
    S.append(S[i-1]+A[i%N])

def search(r):
    s = S[r]
    l = 0
    while r-l > 1:
        m = (r+l) // 2
        if s-S[m] == target:
            return True
        elif s-S[m] > target:
            l = m
        else:
            r = m
    return False

ans = 'No'
for i in range(N, 2*N-1):
    if search(i):
        ans = 'Yes'
        break
print(ans)
