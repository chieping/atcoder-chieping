from decimal import Decimal
import sys
readline = sys.stdin.readline
X = int(readline())
now = 100
ans = 0
interest = Decimal("1.01")
while now < X:
    now = int(now*interest)
    ans += 1
print(ans)