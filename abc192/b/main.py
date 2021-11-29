import re
S = input()
if re.match(r"^[A-Z]*$", S[1::2]) and re.match(r"^[a-z]*$", S[0::2]):
    print('Yes')
else:
    print('No')
