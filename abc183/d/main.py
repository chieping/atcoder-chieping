from sys import stdin
N, W = map(int, stdin.readline().split())
S = [0] * (2*10**5+1)
for _ in range(N):
    s, t, p = map(int, stdin.readline().split())
    S[s] += p
    S[t] -= p

for i in range(2*10**5):
    S[i+1] += S[i]

print('Yes' if max(S) <= W else 'No')
