K = int(input())
divisors = []

i = 1
while i*i <= K:
    quotient, remainder = divmod(K, i)
    if remainder == 0:
        divisors.append(i)
        if i != quotient:
            divisors.append(quotient)
    i += 1

divisors.sort()

s = set()
for i in divisors:
    for j in divisors:
        tmp = i*j
        if tmp > K:
            continue
        q, r = divmod(K, tmp)
        if r == 0:
            s.add(tuple(sorted((i, j, q))))
print(len(s))
