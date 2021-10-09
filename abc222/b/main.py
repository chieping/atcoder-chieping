N, P = map(int, input().split())
A = list(map(int, input().split()))
print(len(list(filter(lambda x: x < P, A))))
