N, M = map(int, input().split())
A = [0] * M
B = [0] * M
for i in range(M):
    A[i], B[i] = map(lambda x: int(x) - 1, input().split())

if M > N - 1:
    print('No')
    exit()

cnt = [0] * N
parent = [-1] * N

def root(x):
    if parent[x] < 0:
        return x
    parent[x] = root(parent[x])
    return parent[x]

def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return False
    if parent[x] > parent[y]:
        x, y = y, x
    parent[x] += parent[y]
    parent[y] = x
    return True


for a, b in zip(A, B):
    cnt[a] += 1
    cnt[b] += 1
    if not unite(a, b):
        print('No')
        exit()
ans = max(cnt) <= 2
print('Yes' if ans else 'No')