import sys
readline = sys.stdin.readline
X, Y = map(int, readline().split())

# WA
# b2 = Y-2*X
# a2 = -Y+4*X
# if b2 < 0 or a2 < 0:
#     print('No')
# else:
#     print('Yes')

ans = False
for turu in range(X+1):
    kame = X - turu
    if turu * 2 + kame * 4 == Y:
        ans |= True
print('Yes' if ans else 'No')
