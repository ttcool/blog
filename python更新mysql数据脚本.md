#python更新mysql数据脚本
'''python

#! /usr/bin/env python
#coding=utf-8
"""
拼接SQL语句，更新数据库数据
"""
import datetime
import time
import MySQLdb
import sys


def open_file(filename):
    path = ""
    file = open(path+filename)
    return file

# 处理数据库的函数
def mysql_database(sql_str):
    conn = MySQLdb.connect(host='localhost', user='root',passwd='root',charset='utf8')
    cursor = conn.cursor()
    conn.select_db('dj')

    cursor.execute(sql_str)
    conn.commit()
    cursor.close()
    conn.close()


def mdcode(str1):
    for c in ('utf-8', 'gbk', 'gb2312'):
        try:
            return str1.decode(c).encode('utf-8')
        except:
            pass
    return 'unknown'

def parse():
    file = open_file("nianjia.txt")

    SQL = ''

    for i in file:
        temp_list = i.strip().split('|')
        name = temp_list[0]
        holiday = temp_list[1]
        SQL = "update attendance_employee set holiday= '"+ holiday + "' where name = '" + name +"'"
        print SQL   
        mysql_database(SQL) 

if __name__ == '__main__':
    t = time.time()

    parse()

    print "end--",time.time() - t

'''
