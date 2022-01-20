from pprint import pprint
import sys
readline = sys.stdin.readline
N = int(readline())
L = list(map(int, readline().split()))
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            l1, l2, l3 = L[i], L[j], L[k]
            if len(set([l1, l2, l3])) == 3:
                if l1 + l2 + l3 > max(l1, l2, l3)*2:
                    # print(list(map(lambda x: x+1, [i,j,k])))
                    ans += 1
print(ans)
