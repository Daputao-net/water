class Game(object):
    
    #类属性
    num=0

    #实例方法
    def __init__(self):
        #实例属性   
        self.name="laowang"

    @classmethod #类方法的标注
    def add_num(cls): #cls可以用任何名字替换
        cls.num=100

    #静态类
    @staticmethod #静态方法的标志（装饰器）
    def print_menu(): #不用传参数
        print("-*10")
        print("  穿越火线V11.1  ")
        print("1.开始游戏")
        print("2.结束游戏")
        print("-*10")

#Game.print_menu() #通过类来调用静态方法
game=Game()
game.print_menu()#通过对象来调用静态方法
#Game.add_num() #类方法可以通过类的名字调用类方法。
game.add_num() #还可以通过这个类创建出来的对象调用类方法。
print(game.num)



