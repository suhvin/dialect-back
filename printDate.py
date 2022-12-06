from datetime import datetime

now  = datetime.now()
date_now = datetime.strptime(str(now.year)+str(now.month)+str(now.day), "%Y%m%d")
print("현재 :", date_now)

date_to_compare = datetime.strptime("20221125", "%Y%m%d")
print("비교할 날짜 :", date_to_compare)

date_diff = date_now - date_to_compare
print("차이 :", date_diff.days)	
print("Day", int(date_diff.days)%2+1)	