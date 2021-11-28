N = int(input())
S = list(input()) + ['.']
ans = 0
prev = S[0]
l = 1
for i in range(1, N+1):
    if S[i] == prev:
        l += 1
    else:
        prev = S[i]
        if l > 1:
            ans += l * (l-1) // 2
        l = 1
print(ans)
