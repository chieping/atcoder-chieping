import sys
input = sys.stdin.readline
T = int(input())
N = [list(input()[:-1]) for _ in range(T)]
for nl in N:
    l = len(nl)
    n = int(''.join(nl))
    candidate = []
    if l > 2:
        candidate.append(10**(l-1)-1)
    for w in range(l//2, 0, -1):
        if l % w != 0: continue
        t = l//w

        chunks = [nl[j:j+w] for j in range(0, l, w)]
        chunk_num = [int(''.join(i)) for i in chunks]

        ok = 0
        ng = chunk_num[0]+1
        while ng - ok > 1:
            mid = (ng+ok)//2
            if int(str(mid) * t) <= n:
                ok = mid
            else:
                ng = mid
        candidate.append(int(str(ok)*t))
    print(max(candidate))
