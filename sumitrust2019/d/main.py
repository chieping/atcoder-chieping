N = int(input())
S = list(map(int, input()))
ans = 0

def f(A):
    i = 0
    while len(A):
        if i == N: break
        if S[i] == A[0]:
            A = A[1:]
        i += 1
    else:
        return True
    return False

for a in range(10):
    for b in range(10):
        for c in range(10):
            ans += f([a, b, c])
print(ans)
