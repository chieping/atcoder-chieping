
N, K = map(int, input().split())

I = K

A = sorted([list(map(int, input().split())) for i in range(N)], key= lambda x: x[0])

for a, b in A:
    if a <= I:
        I += b
    else:
        break

print(I)
