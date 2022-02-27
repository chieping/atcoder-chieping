# WA
import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))

def dfs(i, j, k):
    a = i
    b = j
    c = k
    for l in range(3):
        a, b, c = c, a, b
        # 先頭文字が一致する場合
        if A[a] == B[i]:
            if i+2 == N-1:
                # 最後に残りも一致していればok
                if A[b] == B[j] and A[c] == B[k]:
                    return True
            else:
                bt = A[i:k+1]
                A[i], A[j], A[k] = A[a], A[b], A[c]
                if dfs(j, k, k+1):
                    return True
                A[i:k+1] = bt

    return False

ans = dfs(0, 1, 2)
print('Yes' if ans else 'No')