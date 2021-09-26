N = int(input())
A = list(map(int, input().split()))
MaxA = 200
ans = 0
cnt = [0] * (MaxA*2 + 1)
for i in range(N):
    cnt[MaxA+A[i]] += 1
for i in range(len(cnt)):
    for j in range(i+1, len(cnt)):
        a = i-MaxA
        b = j-MaxA
        ans += cnt[i]*cnt[j]*(a-b)**2
print(ans)
