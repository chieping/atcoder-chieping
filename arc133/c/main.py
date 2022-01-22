# 縦の制約と横の制約それぞれで達成できる可能性のある
# 上限の合計数を求める
# 縦横の合計数のより小さい方は達成可能となるのでそれが答えになる
# 証明はよくわからん
from math import floor
from pprint import pprint
import sys
readline = sys.stdin.readline
H, W, K = list(map(int, readline().split()))
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))

if sum(A) % K != sum(B) % K:
    print(-1)
    exit()

vt = 0
hr = 0

for i in range(H):
    a = A[i]
    c = (K-1) * (W-1)
    c += (a-(c%K))%K
    vt += c

for i in range(W):
    b = B[i]
    c = (K-1) * (H-1)
    c += (b-(c%K))%K
    hr += c

print(min(vt, hr))
