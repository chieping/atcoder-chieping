N = int(input())
A = list(map(int, input().split()))
colors = set()
Any = 0
for a in A:
    if a < 400: colors.add(1)
    elif a < 800: colors.add(2)
    elif a < 1200: colors.add(3)
    elif a < 1600: colors.add(4)
    elif a < 2000: colors.add(5)
    elif a < 2400: colors.add(6)
    elif a < 2800: colors.add(7)
    elif a < 3200: colors.add(8)
    else: Any += 1
Min = len(colors)
if Min == 0:
    Min = int(Any > 0)
Max = len(colors) + Any
print(Min, Max)