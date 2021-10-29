N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
AA = [0] * 46
BB = [0] * 46
CC = [0] * 46

for a in A:
    r = a % 46
    AA[r] += 1
for b in B:
    r = b % 46
    BB[r] += 1
for c in C:
    r = c % 46
    CC[r] += 1

for a in range(0, 46):
    for b in range(0, 46):
        for c in range(0, 46):
            if (a + b + c) % 46 == 0:
                ans += AA[a] * BB[b] * CC[c]

print(ans)

