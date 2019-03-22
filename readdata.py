#coding:utf-8
import info
import csv   #csvモジュールをインポートする
patern = 0
if patern == 0:
    f = open('patern0.csv', 'r')
if patern == 1:
    f = open('patern1.csv', 'r')
if patern == 2:
    f = open('patern2.csv', 'r')
if patern == 3:
    f = open('patern3.csv', 'r')
    dataReader = csv.reader(f)
    mydata = []
    num = 0
    for row in dataReader:
        for col in row:
            if num==0:
                num=1
            else :
                mydata.append(col)
                num = 0
    for t in range(0,10):
        n=100*t+1
        freindship = info.friendship
        before = freindship
        after = float(before + (100-before)*0.8)
        ref = float(after-before)
        floatdata_n = float(mydata[n])

        friendship = int(before+ref*floatdata_n)
        print(before+ref*floatdata_n)
        info.friendship = friendship
