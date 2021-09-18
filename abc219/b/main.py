S = [input() for i in range(3)]
T = list(map(int, list(input())))

for t in T:
    t -= 1
    print(S[t], end='')
print()

