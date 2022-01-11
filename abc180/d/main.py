import sys
readline = sys.stdin.readline
X, Y, A, B = map(int, readline().split())
exp = 0
strength = X
while (strength * A) < (strength + B):
    strength *= A
    if Y <= strength:
        break
    else:
        exp += 1
if Y > strength:
    exp += (Y-strength-1) // B
print(exp)
