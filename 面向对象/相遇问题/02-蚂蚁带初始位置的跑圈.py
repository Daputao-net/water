#定义一个蚂蚁类，这个蚂蚁类有名字属性速度属性和初始位置属性
class Ant(object):

    def __init__(self, name, speed, loca):
        self.name = name
        self.speed = speed
        self.loca = loca
#追及时间=跑道一周的长度÷速度差
def catch(ant1, ant2):
    #time为快的和慢的相遇一次的时间。
    time=0
    time = 1.0/abs(ant1.speed-ant2.speed)
    return time


#相遇的次数=总时间÷追及时间
#此题中次数为浮点数则为未完成，所以采用地板除。
def count_time(i, ant, temp, run_time, total_time):
    #计算第一次追上的时间
    one_catch_time = (1 - ant[temp].loca + i.loca) / abs(i.speed - ant[temp].speed)
    #第一次追上的时间得出后就可以从第一次追上之后作为起点开始计算，计算得出的次数加一即可。
    catch_time = catch(i, ant[temp])
    catch_num = (run_time-one_catch_time) // catch_time + 1
    total_time.append(catch_num)
    print("%s<-->%s:相遇一次的时间为%.2f分钟,%s分钟内相遇%s次" % (i.name, ant[temp].name, float(catch_time), run_time, catch_num))


def main():

    num = 0
    #记录所有蚂蚁之间两两相遇的次数。
    total_time = []

    #创建蚂蚁A，让蚂蚁A以速度1圈/分跑起来
    A = Ant("蚂蚁A", 1, 0)

    # 创建蚂蚁B，让蚂蚁B以速度1.5圈/分跑起来
    B = Ant("蚂蚁B", 1.5, 0.25)

    # 创建蚂蚁C，让蚂蚁A以速度2圈/分跑起来
    C = Ant("蚂蚁C", 2, 0.5)

    # 创建蚂蚁D，让蚂蚁D以速度2.5圈/分跑起来
    D = Ant("蚂蚁D", 2.5, 0.75)

    ant = [A, B, C, D]
    run_time = float(input("请输入蚂蚁跑步的时间："))

    for i in ant:
        if i == A:
            for temp in range(1, 4):
                count_time(i, ant, temp, run_time, total_time)

        elif i == B:
            for temp in range(2, 4):
                count_time(i, ant, temp, run_time, total_time)

        elif i == C:
            for temp in range(3, 4):
                count_time(i, ant, temp, run_time, total_time)

    for i in total_time:

        num += i

    print("在%s分钟后四只蚂蚁两两相遇的次数为：%s" % (run_time, num))

if __name__ == '__main__':
    while True:
        main()