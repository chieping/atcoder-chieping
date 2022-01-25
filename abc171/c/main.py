N = int(input())
ans = []
while N > 0:
    N -= 1
    d, r = divmod(N, 26)
    ans.append(chr(97+r))
    N = d

print(''.join(ans[::-1]))
