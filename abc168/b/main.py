K = int(input())
S = input()
elip = '...' if len(S) > K else ''
K = min(K, len(S))
print(S[:K] + elip)