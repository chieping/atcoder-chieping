_, K = input().split()
K = int(K)
for i, c in enumerate(input()):
    if K-1 == i:
        print(c.lower(), end='')
    else:
        print(c, end='')
print()

