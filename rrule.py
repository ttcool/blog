# coding: utf-8
from datetime import datetime
from dateutil.rrule import rrule,DAILY,MO,WE
#获取2015-8-9至2015-9-9之间所有周一和周三的日期对象
def main():
    rrule_obj = rrule(DAILY,byweekday=(MO,WE),dtstart=datetime(2015,8,9),until=datetime(2015,9,9))
    for i in rrule_obj:
        print i

if __name__ == '__main__':
    main() 
