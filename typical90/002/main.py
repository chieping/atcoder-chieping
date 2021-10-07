N = int(input())

def check(candidate):
    dep = 0
    for s in candidate:
        if s == '(':
            dep += 1
        else:
            dep -= 1
        if dep < 0:
            return False
    return dep == 0


for i in range(2**N):
    candidate = ''
    for j in range(N-1, -1, -1):
        if i & (1<<j) == 0:
            candidate += '('
        else:
            candidate += ')'
    if check(candidate):
        print(candidate)
