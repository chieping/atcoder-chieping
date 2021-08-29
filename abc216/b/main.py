N = int(input())

ST = [input() for i in range(N)]

S = set(ST)

if len(S) < N:
    print('Yes')
else:
    print('No')
