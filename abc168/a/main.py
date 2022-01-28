N = int(input())
N1 = N % 10
if N1 in [2, 4, 5, 7, 9]:
    print('hon')
elif N1 in [0, 1, 6, 8]:
    print('pon')
else:
    print('bon')
