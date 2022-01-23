import sys
readline = sys.stdin.readline
S = list(readline()[:-1])
a, b = map(int, readline().split())
S[a-1], S[b-1] = S[b-1], S[a-1]
print(''.join(S))