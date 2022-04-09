import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
A = list(zip(A, range(N)))
A.sort(key=lambda x: (x[0], -x[1]))
ans = []
j = -1
for a, i in A:
    if K > i:
        j = max(j, i)
    else:
        if j >= 0:
            ans.append(i-j)

if ans:
    print(min(ans))
else:
    print(-1)