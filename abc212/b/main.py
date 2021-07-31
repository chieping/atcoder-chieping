X = list(map(int, list(input())))

if len(set(X)) == 1:
    print('Weak')
elif (X[0] + 1) % 10 == X[1] and (X[1] + 1) % 10 == X[2] and (X[2] + 1) % 10 == X[3]:
    print('Weak')
else:
    print('Strong')
