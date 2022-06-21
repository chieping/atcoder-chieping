# 解説AC
N, K = map(int, input().split())
A = list(map(int, input().split()))
C = [0] * 40
for a in A:
    for i in range(40):
        if a >> i & 1:
            C[i] += 1
z = 0
s = 0
for i in range(40)[::-1]:
    if K >> i & 1:
        t = 0
        for j in range(i):
            t += max(C[j], N - C[j]) << j
        z = max(z, s + (C[i] << i) + t)
        s += (N - C[i]) << i
    else:
        s += C[i] << i

print(max(z, s))
