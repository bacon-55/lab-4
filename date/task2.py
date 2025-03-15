from datetime import datetime, timedelta

print("Yesterday:",datetime.now()-timedelta(1))
print("Today",datetime.now())
print("Tomorrow",datetime.now()+timedelta(1))