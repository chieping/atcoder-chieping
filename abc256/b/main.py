N = int(input())
A = list(map(int, input().split()))
B = [0] * N
for i, a in enumerate(A):
    for j in range(0, i+1):
        B[j] += a
print(sum([b >= 4 for b in B]))
