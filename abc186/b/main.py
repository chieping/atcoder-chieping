from sys import stdin
H, W = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(H)]
_sum = sum(map(sum, A))
_min = min(map(min, A))
print(_sum - _min*H*W)
