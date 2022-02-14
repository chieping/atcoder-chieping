N = int(input())
A = list(map(int, input().split()))
res = all(a % 3 == 0 or a % 5 == 0 for a in A if a % 2 == 0)
print('APPROVED' if res else 'DENIED')