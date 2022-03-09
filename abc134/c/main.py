import sys
readline = sys.stdin.readline
N = int(readline())
A = [int(readline()) for _ in range(N)]
sec, fst = sorted(A)[-2:]

for a in A:
    if fst == a:
        print(sec)
    else:
        print(fst)