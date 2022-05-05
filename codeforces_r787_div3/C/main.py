t = int(input())
for _ in range(t):
    s = input()
    Len = len(s)
    start = 0 # 最後の1
    end = Len-1 # 最初の0
    if '1' in s:
        start = s[::-1].index('1')
        start = Len - 1 - start
    if '0' in s:
        end = s.index('0')
    # print(start, end)
    print(end-start+1)