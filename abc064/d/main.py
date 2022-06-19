N = int(input())
S = input()
a = 0
lowest = 0

for c in S:
    if c == '(':
        a += 1
    else:
        a -= 1
        lowest = min(lowest, a)

ans = abs(lowest) * '(' + S + (a + abs(lowest)) * ')'

print(ans)
