# cpython (pypy7.3.0ではセイウチ演算子が使えない)
import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
acc = 0
S = [acc := acc+n for n in A]
MOD = 10**9+7
ans = 0
for i in range(N):
    ans += A[i] * (S[-1]-S[i])
    ans %= MOD
print(ans)
