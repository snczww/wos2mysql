# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:51:32 2017

@author: zww
任务需求，把mysql的wos数据读取，然后使用spacy分词在写会数据库用,分割
"""

import pymysql
import csv
#import spacy


def query_data():
    db = pymysql.connect('localhost', 'root', '890', 'zls', charset='utf8')
    cursor = db.cursor()
    sql='SELECT TI,AB,GA FROM zl'
    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(results)
        #print(sql)
    
    except Exception as e:
        print('数据库读取异常', e)
    db.close()
    return results
def update_to_sql (column,value,UT):   
    db = pymysql.connect('localhost', 'root', '890', 'zls', charset='utf8')
    cursor = db.cursor()
    sql='UPDATE zlm SET `%s`="%s" WHERE zlGA="%s"' % (column,value,UT)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print('插入数据成功')
    
    except Exception as e:
        print('插入数据异常', e)
        db.close()

def inser_to_sql (UT,TI):   
    db = pymysql.connect('localhost', 'root', '890', 'zls', charset='utf8')
    cursor = db.cursor()
    sql='INSERT INTO zlm(zlGA,zlAB)  VALUES ("%s","%s")' % (UT,TI)
    try:
        cursor.execute(sql)
        db.commit()
        print('插入数据成功')
    
    except Exception as e:
        print('插入数据异常', e)
        db.close()


def xh(TI,UT,AB):
    for j in list1:
        j=str(j)
        k=0
        if j[2:len(j)-2].replace('_',' ') in str(AB):
            k=1
            print(11111111)
            
            #update_to_sql (j[2:len(j)-2],k,UT)
        #j=str(j)
        #print(j[2:len(j)-3].replace('_',' '))

        #update_to_sql (j[2:len(j)-2],k,UT)
        return
        
        
        
def fu(i):
    TI=results[i][0]
    TI=TI.replace('\'', '').replace('\"', '').strip('()"')
    UT=results[i][2]
    AB=results[i][1]
    AB=AB.replace('\'', '').replace('\"', '').strip('()"')
    xh(results[i][0],results[i][2],AB)
    #print(UT)      
    #i+=1
        
out=open('out.txt','w')        
list1 = csv.reader(open('zlm.csv', encoding='utf-8'))
word_list=list(list1)
results=query_data()
for i in range(len(results)):
    UT=results[i][2]
    out.write(UT)
    out.write(',')
    print(UT)
    for j in range(len(word_list)):
        #print(i,word_list[j])
        TI=results[i][0]
        TI=TI.replace('\'', '').replace('\"', '').strip('()"')
       
        AB=results[i][1]
        AB=AB.replace('\'', '').replace('\"', '').strip('()"')
        #inser_to_sql (UT,TI)
    #xh(results[i][0],results[i][2],AB)
    #print(UT)

        l=str(word_list[j])
        k=0
        if (l[2:len(l)-2].replace('_',' ')).lower() in str(TI).lower():
            k=1
            out.write(l[2:len(l)-2].replace('_',' '))
            print(l[2:len(l)-2].replace('_',' '))
            out.write(',')
            #outl[i].append(l[2:len(l)-2].replace('_',' '))
        if (l[2:len(l)-2].replace('_',' ')).lower() in str(AB).lower():
            print(l[2:len(l)-2].replace('_',' '))
            out.write(l[2:len(l)-2].replace('_',' '))
            out.write(',')
            #outl[i].append(l[2:len(l)-2].replace('_',' '))
            #update_to_sql (l[2:len(l)-2],k,UT)
    out.write('\n')
        #j=str(j)
        #print(j[2:len(j)-3].replace('_',' ')
        #print(l)
        #update_to_sql (l[2:len(l)-2],k,UT)
        
out.close()
        
'''      
def get_FC(text):
    s=''
    b= nlp(text)
    for np in b.noun_chunks:
        #print(np)
        s=s+str(np)+','
    return s      
        
#nlp=spacy.load('en')
results=query_data()

F = open("tmp.txt", "w") 
for i in range(len(results)):
    t=str(results[i][0]).replace('\'', '').replace('\"', '').strip('()"')
    print(t[:-1])
    print('')
    FC=get_FC(t)
    print(FC)
    print('')
    F.write(t[:-1] + "\n")
    F.write(FC + "\n")
    F.write('\n')
    update_to_sql (str(results[i][1]).strip('\''),FC)'''