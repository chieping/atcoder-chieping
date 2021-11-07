N = int(input())
V = [list(map(int, input().split())) for i in range(N)]
ans = set()

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)    

for i in range(N):
    for j in range(i+1, N):
        a = V[i]
        b = V[j]
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        if dx == 0:
            ans.add((0, 1))
            ans.add((0, -1))
        elif dy == 0:
            ans.add((1, 0))
            ans.add((-1, 0))
        else:
            gcdr = gcd(dx, dy)
            ans.add((dx // gcdr, dy // gcdr))
            ans.add(((-1*dx) // gcdr, (-1*dy) // gcdr))

print(len(ans))

