X = int(input())
h1000 = X // 500
X %= 500
h5 = X // 5
print(h1000 * 1000 + h5 * 5)