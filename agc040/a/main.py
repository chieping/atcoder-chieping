S = input()
N = len(S)
A = [0] * (N+1)

lt = 0
for i, c in enumerate(S):
    if c == '<':
        lt += 1
        A[i+1] = max(A[i+1], lt)
    else:
        lt = 0

gt = 0
for i, c in zip(range(N, 0, -1), S[::-1]):
    if c == '>':
        gt += 1
        A[i-1] = max(A[i-1], gt)
    else:
        gt = 0

print(sum(A))
