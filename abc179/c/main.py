N = int(input())

ans = 0

for A in range(1, N):
    b_cnt = (N-1) // A
    ans += b_cnt

print(ans)
