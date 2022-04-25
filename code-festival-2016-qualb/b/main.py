N, A, B = map(int, input().split())
S = input()
cnt = A+B
for c in S:
    if c == 'a':
        if cnt > 0:
            print('Yes')
            cnt -= 1
        else:
            print('No')
    elif c == 'b':
        if cnt > 0 and B > 0:
            print('Yes')
            cnt -= 1
            B -= 1
        else:
            print('No')
    else:
        print('No')