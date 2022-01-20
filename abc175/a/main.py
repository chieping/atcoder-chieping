import re
m = re.search('R+', input())
if m:
    print(len(m[0]))
else:
    print(0)
