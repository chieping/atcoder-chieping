N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# 片方に火を付けたときにすべてが燃えきる時間を求める

T = 0
for i in range(N):
    T += A[i] / B[i]

# Tの半分の時間時点での左端からの距離を求める

T /= 2
ans = 0

for i in range(N):
    if T <= 0:
        break
    t = A[i] / B[i]
    if T >= t:
        ans += A[i]
        T -= t
    else:
        ans += B[i] * T
        T = 0
print(ans)
