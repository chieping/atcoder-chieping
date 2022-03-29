S = input()
S12 = int(S[:2])
S34 = int(S[2:])
if 0 < S12 <= 12 and 0 < S34 <= 12:
    print('AMBIGUOUS')
elif 0 < S12 <= 12:
    print('MMYY')
elif 0 < S34 <= 12:
    print('YYMM')
else:
    print('NA')