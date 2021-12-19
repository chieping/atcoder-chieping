S = list(input())
T = list(input())
SI = list(map(ord, S))
TI = list(map(ord, T))
a = ord('a')
z = ord('z')
ans = False
for i in range(26):
    SI = [x+1 if x < z else a for x in SI]
    ans |= SI == TI
print('Yes' if ans else 'No')
