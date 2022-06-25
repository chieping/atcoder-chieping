N, X = map(int, input().split())

S = ''
for i in range(65, 99):
    S += chr(i) * N
print(S[X-1])