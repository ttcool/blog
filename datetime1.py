# coding: utf-8
from datetime import datetime,timedelta,date
from dateutil.relativedelta  import relativedelta
#下个月的最后一天= 下两个月的第一天的前一天
def main():
    now_time = date(2015,12,5)
    print now_time
    if now_time.month in [11,12]:
        first_day_of_after_two_month = datetime(now_time.year+1,now_time.month+2-12,1)
    else:
        first_day_of_after_two_month = datetime(now_time.year,now_time.month+2,1)
    last_day_of_next_month = first_day_of_after_two_month - timedelta(days=1)
    print last_day_of_next_month.date()

def main1():
    now_time = date(2015,12,5)
    print now_time
    last_day_of_next_month = now_time + relativedelta(months=2,day=1,days=-1)
    print last_day_of_next_month

if __name__ == '__main__':
    main()
    print "-------"
    main1()
