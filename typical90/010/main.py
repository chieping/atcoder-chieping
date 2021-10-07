N = int(input())
c1sum = [0]
c2sum = [0]

for i in range(N):
    c, p = map(int, input().split())
    c1 = 0
    c2 = 0
    if c == 1:
        c1 = p
    else:
        c2 = p
    c1sum.append(c1sum[-1] + c1)
    c2sum.append(c2sum[-1] + c2)

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(c1sum[r] - c1sum[l-1], c2sum[r] - c2sum[l-1])
    
