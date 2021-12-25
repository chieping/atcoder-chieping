L, R = map(int, input().split())
S = list(input())

ans = S[:L-1] + list(reversed(S[L-1:R])) + S[R:]
print(''.join(ans))
