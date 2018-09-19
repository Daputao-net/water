class Test(object):
    def __init__(self):
        self.__num=100

    def setNum(self,newNum):
        print("-----1------")
        self.__num=newNum

    def getNum(self):
        print("-----2------")
        return self.__num

    num=property(getNum,setNum)
    #经过测试发现property()中的参数位置很重要，它取决于具体的方法实现中的内容
t=Test()
t.setNum(50)
print(t.getNum())
print("_"*50)

t.num=200
print(t.bum)
