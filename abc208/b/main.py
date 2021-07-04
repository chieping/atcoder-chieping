import math

P = int(input())

kouka = 0
remainder = P

for i in range(10, 0, -1):
    if remainder == 0:
        break
    n = math.factorial(i)
    while remainder >= n:
        remainder -= n
        kouka += 1

print(kouka)
