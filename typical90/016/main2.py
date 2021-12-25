# PythonだとTLEする。PyPyだと通る
N = int(input())
A, B, C = map(int, input().split())
ans = 10000
for i in range(10000):
    for j in range(10000-i):
        q, r = divmod(N-(A*i + B*j), C)
        if r == 0 and q >= 0 and i+j+q < 10000:
            ans = min(ans, i+j+q)
print(ans)
