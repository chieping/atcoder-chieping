from collections import Counter
S = input()
C = Counter(S)
for value, cnt in C.items():
    if cnt == 1:
        print(value)
        exit()
print(-1)