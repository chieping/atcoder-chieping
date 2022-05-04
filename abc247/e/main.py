# 解説AC
N, mx, mn = map(int, input().split())
A = list(map(int, input().split()))

def calc(B):
    i, j, countMx, countMn, res = 0, 0, 0, 0, 0
    while i != len(B):
        while j != len(B) and (countMx == 0 or countMn == 0):
            if B[j] == mx:
                countMx += 1
            if B[j] == mn:
                countMn += 1
            j += 1
        if countMx > 0 and countMn > 0:
            res += len(B) + 1 - j
        if B[i] == mx:
            countMx -= 1
        if B[i] == mn:
            countMn -= 1
        i += 1
    return res
    
ans = 0
i = 0
while i != N:
    B = []
    while i != N and mn <= A[i] <= mx:
        B.append(A[i])
        i += 1
    if len(B):
        ans += calc(B)
    else:
        i += 1
print(ans)
