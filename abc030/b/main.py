H, M = map(int, input().split())
L = M / 60 * 360
H = ((H%12)*60+M) / 720 * 360
print(min(abs(H-L), 360 - abs(H-L)))