import math

N = int(input())

d = math.ceil(N / 9)
m = N % 9
if m == 0:
    m = 9

ans = ""

for i in range(0, d):
    ans += str(m)

print(ans)
