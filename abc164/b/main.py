A, B, C, D = map(int, input().split())
t = True
while A > 0 and C > 0:
    if t:
        C -= B
    else:
        A -= D
    t = not t
print('Yes' if not t else 'No')
