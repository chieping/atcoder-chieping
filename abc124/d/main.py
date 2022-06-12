from itertools import accumulate
N, K = map(int, input().split())
S = list(map(int, list(input()))) 
run_length = []
now = 1
Len = 0
for c in S:
    if c == now:
        Len += 1
    else:
        run_length.append(Len)
        Len = 1
        now = c
if Len != 0:
    run_length.append(Len)
# 必ず1の長さで終わるようにする
if now == 0:
    run_length.append(0)

ans = 0
cum = [0] + list(accumulate(run_length))
for i in range(0, len(run_length), 2):
    ans = max(ans, cum[min(i + 2*K+1, len(run_length))] - cum[i])
print(ans)
