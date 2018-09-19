class CarStore(object):
    def order(self,money):
        if money>=50000 and money<100000:
            return Car()#创建了一个对象，把引用返回。

        if money>=1000000 and money<3000000:
            return Car1()#创建了一个对象，把引用返回。

        if money>500000 and money<1000000:
            return Car2()#创建了一个对象，把引用返回。

        if money>15000000:
            return Car3()#创建了一个对象，把引用返回。

class Car(object):#对象没有在外面直接创建，而是通过上面的方法返回一个对象。
    def name(self):
        print("AE86")
    def move(self):
        print("车在移动...")
    def music(self):
        print("正在播放音乐...")
    def stop(self):
        print("车在停止...")

class Car1(Car): 
    def name(self): 
        print("梅赛德斯奔驰")
    
class Car2(Car): 
    def name(self): 
        print("BWM")
class Car3(Car): 
    def name(self): 
        print("布加迪威龙")

while True:
    money=int(input("您有多少钱："))
    car_store=CarStore()
    car=car_store.order(money)
    car.name()
    car.move()
    car.music()
    car.stop()

