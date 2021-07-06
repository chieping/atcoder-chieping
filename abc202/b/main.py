S = input()

def rotate(n):
    if n == '6':
        return '9'
    elif n == '9':
        return '6'
    else:
        return n

print(''.join(map(rotate, reversed(S))))
