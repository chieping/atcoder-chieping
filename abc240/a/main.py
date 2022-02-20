A, B = map(int, input().split())

g = max(A, B)
s = min(A, B)

if g == 10 and s == 1:
    print('Yes')
elif s + 1 == g:
    print('Yes')
else:
    print('No')