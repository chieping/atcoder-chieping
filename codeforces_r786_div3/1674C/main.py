import sys
input = sys.stdin.readline
q = int(input())
for _ in range(q):
    s = input()[:-1]
    t = input()[:-1]
    if t == 'a':
        print(1)
        continue
    if 'a' in t:
        print(-1)
        continue
    print(2**len(s))

