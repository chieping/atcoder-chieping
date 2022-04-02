A = list(input())
A.sort(reverse=True)
a = b = []
for i in range(len(A)):
    if i % 2:
        a.append(A[i])
    else:
        b.append(A[i])
print(int(''.join(a))*int(''.join(b)))