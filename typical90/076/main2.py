from bisect import bisect_left
from sys import stdin
N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
_sum = sum(A)
target = _sum // 10
# 割り切れない場合はNo確定
if _sum % 10 != 0:
    print('No')
    exit()

# Aを2倍した累積和
Asum2 = [A[0]]
for a in A[1:]+A:
    Asum2.append(Asum2[-1]+a)

for l in range(N*2):
    idx = bisect_left(Asum2, Asum2[l]+target)
    if idx <= N*2-1 and Asum2[idx] == Asum2[l] + target:
        print('Yes')
        exit()

print('No')
