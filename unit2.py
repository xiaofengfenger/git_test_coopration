
# -*- coding:utf-8 -*-
#**第 0002 题**：将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。


import MySQLdb


def store_sql(filepath):
    db=MySQLdb.connet(host="localhost",user="yin",passwd="123",db="testdb")
    cursor=db.cursor()          #类似于操作数据库的指针
    cursor.execute("show tables in testdb;")
    tables=cursor.fetchall()
    findtables=False
    for table in tables:
        if 'code' in table:
            findtables=True
            print("table already exits")
    if not findtables:
        cursor.excute("CREAT TABLE code(
        id INT NOT NULL AUTO_INCREMENT,
        code VARCHAR(10)
        PRIMARY KEY(id)
        );"
        )
    f=open(filepath,'rb')
    for line in f.readlines():
        coupon=line.strip()
        cursor.execute("INSERT INTO code VALUES(%s);",[coupon])

    db.commit()
    cursor.close()
    db.close()


    if __name__='__main__':
        store_sql('Running_result.txt')
