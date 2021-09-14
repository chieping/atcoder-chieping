N = int(input())
P = list(map(int, input().split()))
s = 1
for p in P:
    s |= s << p
print(bin(s).count("1"))
