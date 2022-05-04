from math import factorial


for n in range(7):

    fact = []

    nf = factorial(n)

    i = 1
    while i*i <= nf:
        d, r = divmod(nf, i)
        if r == 0:
            fact.append(i)
            if d != i:
                fact.append(d)
        i += 1
    print(f'{n}: {len(fact)}: {sorted(fact)}')


