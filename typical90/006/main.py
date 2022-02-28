N, K = map(int, input().split())
S = input()
Sint = list(map(ord, S))
ans = []
left = 0

for i in range(N-K, N):
    MIN = 10000
    for j in range(left, i+1):
        now = Sint[j]
        if now < MIN:
            left = j+1
            MIN = now
    ans.append(MIN)

print(''.join(map(chr, ans)))