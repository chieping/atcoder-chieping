n = int(input())
A = []
B = []

for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

W = [0] * 1_000_100

for i in range(n):
    W[A[i]] += 1
    W[B[i]+1] -= 1

for i in range(1, len(W)):
    W[i] = W[i] + W[i-1]

print(max(W))
