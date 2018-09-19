class CarStore(object):
    def order(self,car_type):
        return select_car_by_type(car_type)#创建了一个对象，把引用返回。 
def select_car_by_type(car_type):
    if car_type=="索纳塔":
        return Suonata()
    elif car_type=="名图":
        return Mingtu()
    elif car_type=="ix35":
        return Ix35()

class Car(object):#对象没有在外面直接创建，而是通过上面的方法返回一个对象。
    def move(self):
        print("车在移动...")
    def music(self):
        print("正在播放音乐...")
    def stop(self):
        print("车在停止...")

class Suonata(Car):
    def name(self):
        print("索纳塔...")
    
    def money(self):
        print("售价50000~80000RMB...")

class Mingtu(Car):
    
    def name(self):
        print("名图...")
    
    def money(self):
        print("售价100000~150000RMB...")


class Ix35(Car):

    def name(self):
        print("ix35...")
    
    def money(self):
        print("售价200000~230000RMB...")

while True:
    car_store=CarStore()
    car_type=str(input("请输入您要选择的车辆类型："))
    car=car_store.order(car_type)
    car.name()
    car.money()
    car.move()
    car.music()
    car.stop()

