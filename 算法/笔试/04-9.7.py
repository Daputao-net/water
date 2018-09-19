
def check_time(li):
    """判断时间"""
    if 0 <= int(li[0]) <= 23 and 0 <= int(li[1]) <= 59 and 0 <= int(li[2]) <= 59:

        print("%2s:%2s:%2s" % (li[0], li[1], li[2]))
    else:
        if int(li[0]) > 23 or int(li[0]) < 0:
            li[0] = int(li[0]) % 10
        if int(li[1]) > 59 or int(li[1]) < 0:
            li[1] = int(li[1]) % 10
        if int(li[2]) > 59 or int(li[2]) < 0:
            li[2] = int(li[2]) % 10
        for i in range(3):
            li[i] = int(li[i])
        print("%02d:%02d:%02d" % (li[0], li[1], li[2]))
# 输入的次数
n = int(input())

time = []
new = []
for i in range(n):
    time.append(input())
    new.append(time[i].split(":"))
# print(new)
for i in range(n):
    check_time(new[i])





# import time
# import datetime
#
# a = input('请输入日期，格式为yyyy-mm-dd')
# t = time.strptime(a, "%Y-%m-%d")
# y, m, d = t[0:3]
# print(datetime.datetime(y, m, d))