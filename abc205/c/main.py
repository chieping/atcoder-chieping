A, B, C = map(int, input().split())

if A == B or (abs(A) == abs(B) and C%2==0):
    print('=')
else:
    if C % 2 == 0:
        C = 2
    else:
        C = 3
    if A**C > B**C:
        print('>')
    else:
        print('<')
