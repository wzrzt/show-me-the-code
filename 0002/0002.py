# --*utf-8*

import random
import pymysql

char = "1234567890poiuytrewqasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM"


def get_coupon(length, char):
    coupon = ""
    for i in range(0, length):
        coupon = coupon + random.choice(char)
    return coupon


def create_coupon_table():

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "7777", "test")

    try:
        with db.cursor() as cursor:
            # 使用cursor()方法获取操作游标
            # 如果数据表已经存在使用 execute() 方法删除表。
            sql1 = """drop table if exists test.coupon_table;
                create table test.coupon_table(id int not null auto_increment, code varchar(30), primary key (id));
                """
            cursor.execute(sql1)
        db.commit()

    finally:
        db.close()


def save_to_sql(coupon):

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "7777", "test")

    try:
        with db.cursor() as cursor:
            # 使用cursor()方法获取操作游标
            # 如果数据表已经存在使用 execute() 方法删除表。
            sql2 = """insert into test.coupon_table(code) values(%s)"""
            cursor.execute(sql2, coupon)
        db.commit()

        # with conn.cursor() as cursor:
        #     # Read a single record
        #     sql = "SELECT * FROM `codes` "
        #     cursor.execute(sql)
        #     result = cursor.fetchone()
        #     print(result)

    finally:
        db.close()


def show_result():
    db = pymysql.connect("localhost", "root", "7777", "test")

    try:
        sql = """select * from test.coupon_table;"""
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    finally:
        db.close()

    return result


def main():
    length = int(input("input length: "))
    num = int(input("input num: "))
    create_coupon_table()
    couponlist = list()
    for i in range(0, num):
        coupon = get_coupon(length, char)
        couponlist.append(coupon)

    for coupon in couponlist:
        save_to_sql(coupon)

    return show_result()


if __name__ == '__main__':
    print(main())

