N, X = map(int, input().split())
S = input()
now = list(format(X, 'b'))

for c in S:
    if c == 'U':
        now.pop()
    elif c == 'L':
        now.append('0')
    elif c == 'R':
        now.append('1')

print(int(''.join(now), 2))