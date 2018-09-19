class Base(object): 
    def test(self):
        print("----Base")
class A(Base):
    def test(self):
        print("----A")
class B(Base):
    def test(self):
        print("----B")

class C(A,B):
    pass
    #def test(self):
        #print("----c")

c=C()
c.test()
#这个函数决定了调用一个方法的时候调用的顺序，如果在某个类中中到了方法，就停止调用。c3算法实现。
print(C.__mro__)

#尽量保证类中没有相同的方法。
