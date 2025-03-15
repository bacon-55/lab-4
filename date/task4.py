import datetime
time1 = input("Input first date: ")
time2 = input("Input second date: ")
format = "%Y-%m-%d %H:%M:%S"
ans1 = datetime.datetime.strptime(time1, format)
ans2 = datetime.datetime.strptime(time2, format)
print("difference in seconds:",abs(ans1-ans2).total_seconds())