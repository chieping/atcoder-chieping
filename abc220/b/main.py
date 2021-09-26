K = int(input())
A, B = input().split()
A = list(map(int, A))
B = list(map(int, B))
A10 = 0
B10 = 0
while len(A) > 0:
    A10 *= K
    A10 += A.pop(0)
while len(B) > 0:
    B10 *= K
    B10 += B.pop(0)
print(A10 * B10)
