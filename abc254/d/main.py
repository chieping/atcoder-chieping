N = int(input())
cnt = [0] * (N+1)
for i in range(1, N+1):
    val = i
    j = 2
    while j*j <= val:
        if val % (j*j) == 0:
            val //= j*j
        else:
            j += 1
    cnt[val] += 1

print(sum(c*c for c in cnt))
