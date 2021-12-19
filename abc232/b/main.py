S = list(input())
T = list(input())
SI = list(map(ord, S))
TI = list(map(ord, T))

for i in range(26):
    SI = list(map(lambda x: x+1 if x < 122 else 97, SI))
    if SI == TI:
        print('Yes')
        exit()
print('No')
