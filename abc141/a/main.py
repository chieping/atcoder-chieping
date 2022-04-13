S = input()
A = ['Sunny', 'Cloudy', 'Rainy']
i = A.index(S)
print(A[(i+1)%3])