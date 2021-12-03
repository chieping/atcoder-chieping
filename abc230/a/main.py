N = int(input())

if N < 42:
    if N < 10:
        print('AGC00' + str(N))
    else:
        print('AGC0' + str(N))
else:
    print('AGC0' + str(N+1))
