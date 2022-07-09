S = input()
T = input()
SLen = len(S)
TLen = len(T)

# ランレングス
Sr = []
prev = '0'
l = 1
for c in S:
    if prev == c:
        l += 1
    else:
        Sr.append((prev, l))
        l = 1
        prev = c
Sr.append((prev, l))

Tr = []
prev = '0'
l = 1
for c in T:
    if prev == c:
        l += 1
    else:
        Tr.append((prev, l))
        l = 1
        prev = c
Tr.append((prev, l))

if len(Sr) != len(Tr):
    print('No')
    exit()

for i in range(len(Sr)):
    if Sr[i][0] != Tr[i][0]:
        print('No')
        exit()
    if Sr[i][1] == 1 and Tr[i][1] > 1:
        print('No')
        exit()
    if Sr[i][1] > Tr[i][1]:
        print('No')
        exit()
print('Yes')