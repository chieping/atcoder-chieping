N = int(input())
R = []
G = []
B = []

for _ in range(2*N):
    a, c = input().split()
    a = int(a)
    if c == 'R':
        R.append(a)
    elif c == 'G':
        G.append(a)
    elif c == 'B':
        B.append(a)
R.sort()
G.sort()
B.sort()

if len(R) % 2 == 0 and len(B) % 2 == 0:
    print(0)
    exit()

def f(C1, C2):
    now = 10**18
    i, j = 0, 0
    while i < len(C1) and j < len(C2):
        now = min(now, abs(C1[i]-C2[j]))
        if C1[i] > C2[j]:
            j += 1
        else:
            i += 1
    return now

ans = 0
if len(R) % 2 == 0:
    ans = min(f(G, B), f(R, G) + f(R, B))
elif len(G) % 2 == 0:
    ans = min(f(R, B), f(G, R) + f(G, B))
elif len(B) % 2 == 0:
    ans = min(f(R, G), f(B, G) + f(B, R))
print(ans)
