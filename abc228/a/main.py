S, T, X = map(int, input().split())

if S < T:
    if S <= X < T:
        print('Yes')
    else:
        print('No')
else:
    # T < S
    T += 24
    if X < S:
        X += 24
    if S <= X < T:
        print('Yes')
    else:
        print('No')

