N = int(input())

dn = len(str(N))

if N < 10:
    print(0)
    exit()

if len(str(N)) % 2 == 1:
    print('9' * (len(str(N)) // 2))
    exit()

half = dn // 2

first_half = N // (10**half)
last_half = N % (10**half)

ans = first_half - 1
if first_half <= last_half:
    ans += 1

print(ans)
