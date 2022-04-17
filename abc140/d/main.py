N, K = map(int, input().split())
S = input()
cnt = 0
ans = 0
prev = S[0]
for c in S:
    if prev == c:
        ans += 1
    else:
        cnt += 1
    prev = c
ans -= 1
ans += min(K*2, cnt)
print(ans)