N = int(input())
A = [int(input()) for _ in range(N)]
for i in range(N-1):
    a1, a2 = A[i:i+2]
    if a1 == a2:
        print('stay')
    elif a1 > a2:
        print(f'down {a1-a2}')
    else:
        print(f'up {a2-a1}')