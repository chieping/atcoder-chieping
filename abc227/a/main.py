N, K, A = map(int, input().split())
if (A + K -1) % N == 0:
    print(N)
else:
    print((A+K-1)% N) 
