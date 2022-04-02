import sys
input = sys.stdin.readline
N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
rem = [a%X for a in A]
rem.sort(reverse=True)
ans = sum(A)
sub = 0
i = 0
while K > 0 and i < N:
    d = A[i] // X
    sub += min(d, K) * X
    K -= d
    i += 1
if K > 0:
    sub += sum(rem[:min(K, N)])
print(ans-sub)