S = input()
if any(S[i] == S[i+1] for i in range(3)):
    print('Bad')
else:
    print('Good')