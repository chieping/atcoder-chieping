N, H = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
a_max = max(A)
B = [b for b in B if b > a_max]
B.sort(reverse=True)
i = 0
while H > 0 and i < len(B):
    H -= B[i]
    i += 1
if H <= 0:
    print(i)
else:
    print((H+a_max-1)//a_max + i)
