from bisect import bisect_left
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N):
    a = L[i]
    for j in range(i+1, N):
        b = L[j]
        # ソートしてあるので、a<=bとなっている
        # cの候補は、b <= c < a+b
        r = bisect_left(L, a+b)
        l = j+1
        ans += max(0, r-l)
print(ans)
