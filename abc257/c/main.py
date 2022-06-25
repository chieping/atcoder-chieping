from bisect import bisect, bisect_left
from heapq import heappush


N = int(input())
S = input()
W = list(map(int, input().split()))


adult = []
a_cnt = 0
kid = []
k_cnt = 0

for i in range(N):
    if S[i] == '1':
        a_cnt += 1
        adult.append(W[i])
    else:
        k_cnt += 1
        kid.append(W[i])

adult.sort()
kid.sort()
# print(adult)
# print(kid)
ans = 0
prev = 0
for i, a in enumerate(adult):
    j = bisect_left(kid, a)
    # print('a', a_cnt-i, j)
    ans = max(ans, a_cnt-i+j)
for i, k in enumerate(kid):
    if prev == k:
        continue
    l = bisect_left(adult, k)
    # print('k', a_cnt-l, i)
    ans = max(ans, a_cnt-l+i)

    # +1
    l = bisect_left(adult, k+1)
    # print('k(+1)', a_cnt-l, i+1)
    ans = max(ans, a_cnt-l+i+1)
    
    prev = k

print(ans)