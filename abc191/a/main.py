V, T, S, D = map(int, input().split())
a = V*T
b = V*S
if a <= D <= b:
    print('No')
else:
    print('Yes')
