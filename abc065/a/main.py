X, A, B = map(int, input().split())
D = A - B
if D >= 0:
    print('delicious')
elif abs(D) <= X:
    print('safe')
else:
    print('dangerous')