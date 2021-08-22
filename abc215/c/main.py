from itertools import permutations

S, K = input().split()
K = int(K)
S = list(S)
S.sort()

ans_lst = permutations(S, len(S))
ans = sorted(set(ans_lst))

print(''.join(ans[K-1]))
