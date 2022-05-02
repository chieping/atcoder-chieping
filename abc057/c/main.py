N = int(input())
args = []
i = 1
while i*i <= N:
    d, r = divmod(N, i)
    if r == 0:
        args = [d, i]
    i += 1
print(len(str(sorted(args)[1])))
