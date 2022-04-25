S = ['W'] + list(input())
lw = -1
lb = -1
ans = 0
for i, c in enumerate(S):
    if c == 'W':
        lw += 1
        if lb != -1:
            ans += i - lb
            lb = lw+1
    else:
        if lb == -1:
            lb = i    
print(ans)