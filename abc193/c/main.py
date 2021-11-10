N = int(input())
S = set()
i = 2
while i**2 <= N:
    j = 2
    while i**j <= N:
        S.add(i**j)
        j += 1
    i += 1
print(N-len(S))
