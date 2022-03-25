N = int(input())
SPI = []
for i in range(1, N+1):
    s, p = input().split()
    p = int(p)
    SPI.append((s, p, i))
SPI.sort(reverse=True, key=lambda x: x[1])
SPI.sort(key=lambda x: x[0])
print(*[i for s,p,i in SPI], sep='\n')
