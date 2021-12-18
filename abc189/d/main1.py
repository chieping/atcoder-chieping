N = int(input())
S = [input() for i in range(N)]
ans = 0
for i in range(N-1, -1, -1):
    if S[i] == 'OR':
        ans += 2**(i+1)
print(ans+1)
