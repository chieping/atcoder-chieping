S = 'abcdefghijklmnopqrstuvwxyz'
P = list(map(int, input().split()))

for p in P:
    print(S[p-1], end='')
print()
