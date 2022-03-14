N = int(input())
S = list(input())
T = []
for c in S:
    if not(len(T) and T[-1] == c):
        T.append(c)
print(len(T))
