N = int(input())
A = list(map(int, input().split()))
INF = 10**18
# 行動1を行わない場合のDP
dp1 = [0, INF]
for a in A[1:]:
    prev = dp1[:]
    dp1[0] = prev[1]
    dp1[1] = min(prev[0], prev[1]) + a

# 行動1を行う場合のDP
dp2 = [INF, A[0]]
for a in A[1:]:
    prev = dp2[:]
    dp2[0] = prev[1]
    dp2[1] = min(prev[0], prev[1]) + a
print(min(dp1[1], dp2[0], dp2[1]))
