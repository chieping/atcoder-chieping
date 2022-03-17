
from collections import Counter
cnt = list(Counter(input()).values())
print('Yes' if cnt == [2, 2] else 'No')