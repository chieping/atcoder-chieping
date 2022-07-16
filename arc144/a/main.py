N = int(input())
print(2*N)
a = ((N-1) // 4)
b = N % 4
b = 4 if b == 0 else b
ans = str(b) + ('4' * a)
print(ans)