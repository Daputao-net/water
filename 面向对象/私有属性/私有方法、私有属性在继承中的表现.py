class A:
    def __init__(self):
        self.num1=100
        self.__num2=200
    def test1(self):
        print("_____test1_____")
    def __test2(self):
        print("_____test2_____")
class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)
b=B()
b.test1()
print(b.num1)
b.test4()

