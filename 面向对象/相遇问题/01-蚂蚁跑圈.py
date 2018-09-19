#定义一个蚂蚁类，这个蚂蚁类有名字属性和速度属性
class Ant(object):

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

#环形追及相遇的要点是当快的追上慢的的时候路程差刚好是一圈
#由此我们可以列出一个公式
#1圈=（快的的速度-慢的的速度）*第一次追上的时间
#第一次追上的时间=1圈/(快的的速度-慢的的速度)
#因为相遇之后无论是在那个点下一次都是全新的一次相遇
#所以一段时间内相遇的次数=这段时间/第一次追上的时间
def catch(ant1, ant2):
    #time为快的和慢的相遇一次的时间。
    time=0
    time = 1.0/abs(ant1.speed-ant2.speed)
    return time


def count_time(i, ant, temp, run_time, total_time):
    catch_time = catch(i, ant[temp])
    catch_num = run_time // catch_time
    total_time.append(catch_num)
    print("%s<-->%s:相遇一次的时间为%.2f分钟,%s分钟内相遇%s次" % (i.name, ant[temp].name, float(catch_time), run_time, catch_num))


def main():

    num = 0
    #记录所有蚂蚁之间两两相遇的次数。
    total_time = []

    #创建蚂蚁A，让蚂蚁A以速度1圈/分跑起来
    A = Ant("蚂蚁A", 1)

    # 创建蚂蚁B，让蚂蚁B以速度1.5圈/分跑起来
    B = Ant("蚂蚁B", 1.5)

    # 创建蚂蚁C，让蚂蚁A以速度2圈/分跑起来
    C = Ant("蚂蚁C", 2)

    # 创建蚂蚁D，让蚂蚁D以速度2.5圈/分跑起来
    D = Ant("蚂蚁D", 2.5)

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
    main()


