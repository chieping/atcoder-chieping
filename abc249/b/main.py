S = list(input())
if len(S) != len(set(S)):
    print('No')
    exit()

l = False
u = False

for c in S:
    l |= c.islower()
    u |= c.isupper()

print('Yes' if l and u else 'No')
