N = int(input())
H = list(map(int, input().split()))

now = 0
for h in H:
    if h - now >= 0:
        now = max(now, h-1)
    else:
        print('No')
        exit()

print('Yes')