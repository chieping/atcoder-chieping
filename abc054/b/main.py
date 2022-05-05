N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

def match(a, b):
    for bi, ai in zip(range(M), range(a, a+M)):
        if A[ai][b:b+M] != B[bi]:
            return False
    return True

for i in range(N-M+1):
    for j in range(N-M+1):
        if match(i, j):
            print('Yes')
            exit()
print('No')