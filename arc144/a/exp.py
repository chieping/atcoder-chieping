for N in range(1, 1001):
    M = 2*N
    for i in range(1, 10000000):
        Sum = sum(map(int, list(str(i))))
        if Sum == N:
            Sum = sum(map(int, list(str(i*2))))
            if Sum == M:
                print(N, i, sep='\t')
                break



