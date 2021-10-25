N = int(input())
users = dict()
for i in range(N):
    S = input()
    if not S in users:
        users[S] = True
        print(i+1)
