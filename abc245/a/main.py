A, B, C, D = map(int, input().split())
if A*100+B < C*100+D+1:
    print('Takahashi')
else:
    print('Aoki')