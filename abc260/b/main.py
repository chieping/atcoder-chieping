N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
admission = [False] * N
ABI = list(zip(A, B, range(N)))

def calc(capacity, fn):
    cap = capacity
    ABI.sort(key=fn, reverse=True)
    for _a, _b, i in ABI:
        if not admission[i] and cap > 0:
            admission[i] = True
            cap -= 1

calc(X, lambda x: x[0] * 1000 - x[2])
calc(Y, lambda x: x[1] * 1000 - x[2])
calc(Z, lambda x: (x[0] + x[1]) * 1000 - x[2])

for i, flag in enumerate(admission, 1):
    if flag:
        print(i)
