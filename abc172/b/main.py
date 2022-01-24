S = input()
T = input()
L = len(S)
ans = 0
for i in range(L):
    ans += S[i] != T[i]
print(ans)