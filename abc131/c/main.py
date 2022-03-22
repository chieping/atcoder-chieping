from math import gcd
A, B, C, D = map(int, input().split())
Cnum = B//C - (A-1)//C
Dnum = B//D - (A-1)//D
lcm = C // gcd(C, D) * D
CDnum = B//lcm - (A-1)//lcm
ans = (B - A + 1) - Cnum - Dnum + CDnum
print(ans)