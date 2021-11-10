from collections import defaultdict
N = int(input())
M = defaultdict(int)
ans = 0
i = 2
while i**2 <= N:
    j = 2
    while i**j <= N:
        if M[i**j] == 0:
            M[i**j] = 1
            ans += 1
        j += 1
    i += 1
print(N-ans)
