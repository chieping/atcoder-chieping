S = input()
expected = 'CODEFESTIVAL2016'
print(sum(s != t for s, t in zip(S, expected)))
