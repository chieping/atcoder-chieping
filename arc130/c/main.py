from collections import Counter
a = list(map(int, list(input())))
b = list(map(int, list(input())))
a_len = len(a)
b_len = len(b)

if a_len >= b_len:
    L = Counter(a)
    S = Counter(b)
else:
    L = Counter(b)
    S = Counter(a)
ans_a = ''
ans_b = ''

kuriagari = False
for i in range(min(a_len, b_len)):
    if kuriagari == False:
        pass
    else:



    pass

print(ans_a)
print(ans_b)
