import math
A, B, H, M = map(int, input().split())

ay = math.sin((H*60+M)/720*math.pi*2)*A
ax = math.cos((H*60+M)/720*math.pi*2)*A

by = math.sin(M/60*math.pi*2)*B
bx = math.cos(M/60*math.pi*2)*B

dist = math.sqrt((ax-bx)**2 + (ay-by)**2)
print(dist)
