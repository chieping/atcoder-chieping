S = input()
L = len(S)
print(sum(S[i] != S[L-1-i] for i in range(L//2)))