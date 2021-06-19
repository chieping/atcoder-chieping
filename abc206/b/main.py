N = int(input())

sum = 0

for i in range(1, 10000000000):
    sum += i
    if N <= sum:
        print(i)
        break


