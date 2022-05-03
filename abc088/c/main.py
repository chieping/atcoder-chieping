C = [list(map(int, input().split())) for _ in range(3)]
c11 = C[0][0]
c12 = C[0][1]
c13 = C[0][2]
c21 = C[1][0]
c22 = C[1][1]
c23 = C[1][2]
c31 = C[2][0]
c32 = C[2][1]
c33 = C[2][2]

Sum = sum(sum(c) for c in C)
if Sum % 3 != 0:
    print('No')
    exit()
Sum //= 3
Sum += 1

for a1 in range(Sum):
    for b1 in range(Sum-a1):
        if c11 != a1+b1:
            continue
        for a2 in range(Sum-a1-b1):
            if c21 != a2+b1:
                continue
            for b2 in range(Sum-a1-b1-a2):
                if c12 != a1+b2:
                    continue
                if c22 != a2+b2:
                    continue
                for a3 in range(Sum-a1-b1-a2-b2):
                    b3 = Sum-a1-a2-a3-b1-b2-1
                    if c31 == a3+b1 and c32 == a3+b2 and c33 == a3+b3 and c13 == a1+b3 and c23 == a2+b3:
                        print('Yes')
                        exit()
print('No')