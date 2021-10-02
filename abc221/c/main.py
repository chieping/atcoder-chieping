s = input()
N = int(s)

nlist = list(map(int, list(s)))
nlist.sort()

A = 0
B = 0

while len(nlist) > 0:
    if A > B:
        B*= 10
        B += nlist.pop()
    else:
        A *= 10
        A += nlist.pop()

print(A*B)

