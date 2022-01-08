from sys import stdin
t = int(stdin.readline())

def f(x):
    return x**2 + 2*x + 3

ans = f(f(f(t)+t) + f(f(t)))

print(ans)
