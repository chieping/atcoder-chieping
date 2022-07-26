from datetime import date, timedelta
dt = date(*list(map(int, input().split('/'))))
while len(set(str(dt))) > 3:
    dt += timedelta(days=1)
print(dt.strftime("%Y/%m/%d"))