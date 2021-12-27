N = int(input())
S = set(input() for _ in range(N))
ans = 'satisfiable'
for s in S:
    if s[0] == '!':
        if s[1:] in S:
            ans = s[1:]
            break
print(ans)
