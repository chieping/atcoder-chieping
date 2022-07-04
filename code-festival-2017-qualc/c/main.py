s = input()
sr = s[::-1]
n = len(s)

if s.replace('x', '') != sr.replace('x', ''):
    print(-1)
    exit()

i = 0
j = n-1
ans = 0
while i < j:
    if s[i] == 'x':
        if s[j] == 'x':
            i += 1
            j -= 1
        else:
            i += 1
            ans += 1
    else:
        if s[j] == 'x':
            j -= 1
            ans += 1
        else:
            i += 1
            j -= 1

print(ans)
