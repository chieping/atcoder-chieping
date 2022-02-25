N = int(input())
H = list(map(int, input().split()))
S = [0]*N
tmp = 0
for i in range(N):
    if H[i] <= tmp:
        if i > 0:
            S[i] = S[i-1] + 1
    else:
        S[i] = 0
    tmp = H[i]
print(max(S))
