A, B = map(int, input().split())

while A > 0 and B > 0:
    a = A % 10
    b = B % 10
    if a + b >= 10:
        print('Hard')
        exit()
    A //= 10
    B //= 10

print('Easy')
