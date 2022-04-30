N = int(input())
A = list(map(int, input().split()))
odd = sum(a % 2 == 1 for a in A)
two = sum(a % 2 == 0 and a % 4 != 0 for a in A)
four = N - odd - two
# print(two, four, odd)

if odd - 1 == four:
    if two % 2 == 0:
        print('Yes')
    else:
        print('No')
elif odd <= four:
    print('Yes')
else:
    print('No')