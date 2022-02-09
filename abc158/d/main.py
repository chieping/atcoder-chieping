import sys
readline = sys.stdin.readline
S = list(readline()[:-1])
Q = int(readline())
rev = False
pre = []
post = []
for _ in range(Q):
    q = readline()[:-1]
    if q[0] == '1':
        rev = not rev
    else:
        f, c = q.split()[1:]
        if f == '1':
            if not rev:
                pre.append(c)
            else:
                post.append(c)
        else:
            if not rev:
                post.append(c)
            else:
                pre.append(c)

ans = ''.join(pre[::-1] + S + post)
if not rev:
    print(ans)
else:
    print(ans[::-1])