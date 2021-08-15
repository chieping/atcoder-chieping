N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# minvalue = 1
# maxvalue = 1000

# for i in range(N):
#     minvalue = max(minvalue, A[i])

minvalue = sorted(A)[-1]
maxvalue = sorted(B)[0]

print(max(0, maxvalue - minvalue + 1))
