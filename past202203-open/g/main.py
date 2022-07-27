a, b, c = map(int, input().split())

def calc(x):
    return a*(x**5) + b*x + c

def binary_search():
    bottom = 1
    top = 2
    mid = 1.5
    for _ in range(200):
        if calc(mid) < 0:
            bottom = mid
            mid += (top-mid) / 2
        else:
            top = mid
            mid -= (mid-bottom) / 2
    return mid

print(binary_search())