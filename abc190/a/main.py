A, B, C = map(int, input().split())

if C == 1:
    C = True

while True:
    if C:
        C = not C
        if B > 0:
            B -= 1
        else:
            print('Takahashi')
            break
    else:
        C = not C
        if A > 0:
            A -= 1
        else:
            print('Aoki')
            break
