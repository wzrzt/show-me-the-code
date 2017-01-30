# --*utf-8*
import random

char = "1234567890poiuytrewqasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM"


def get_coupon(length, char):
    coupon = ""
    for i in range(0, length):
        coupon = coupon + random.choice(char)
    return coupon


def main():
    length = int(input("input length: "))
    num = int(input("input num: "))
#    couponlist = []
    couponlist = list()
    for i in range(0, num):
        coupon = get_coupon(length, char)
        couponlist.append(coupon)

    return couponlist


if __name__ == '__main__':
    print(main())
