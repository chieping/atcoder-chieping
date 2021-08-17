import re

n = input()
p = re.sub(r'0+$', '', n)

if p == p[::-1]:
    print('Yes')
else:
    print('No')
