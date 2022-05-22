from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = list(Counter(A).values())
M = len(B)
ans = 0
i_sum = 0
k_sum = N - B[0]
for j in range(1, M-1):
    i_sum += B[j-1]
    k_sum -= B[j]
    ans += i_sum * B[j] * k_sum
print(ans)
