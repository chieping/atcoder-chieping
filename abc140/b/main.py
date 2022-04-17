N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = sum(B)
prev = -2
for i in A:
    i -= 1
    if prev+1 == i:
        ans += C[prev]
    prev = i
print(ans)