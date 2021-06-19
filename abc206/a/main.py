import math

N = int(input())

n = math.floor(1.08 * N)

if n < 206:
    print('Yay!')
elif 206 == n:
    print('so-so')
else:
    print(':(')
