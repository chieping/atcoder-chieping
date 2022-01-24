from bisect import bisect_left, bisect_right
from itertools import accumulate
from pprint import pprint
import sys
readline = sys.stdin.readline
N, M, K = map(int, readline().split())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
ans = 0
# A, Bそれぞれ累積和を作る
# K - AS[i] でBはいくつ読めるか二分探索で探す
# AをN冊読んだときのBを読める冊数が求まる
Asum = [0] + list(accumulate(A))
Bsum = list(accumulate(B))

for i in range(N+1):
    if Asum[i] > K:
        break
    res = i
    time_to_read = K - Asum[i]
    b = bisect_right(Bsum, time_to_read)
    res += b
    ans = max(ans, res)

print(ans)
