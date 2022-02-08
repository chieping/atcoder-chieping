S = input()
N = len(S)
res1 = S == S[::-1]
T = S[:(N-1)//2]
res2 = T == T[::-1]
U = S[(N+3)//2-1:]
res3 = U == U[::-1]
print('Yes' if res1 and res2 and res3 else 'No')