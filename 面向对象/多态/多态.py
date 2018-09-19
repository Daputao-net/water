class Dog(object):
    def print_self(self):
        print("大家好，我是狗")

class Xiaotq(Dog):
    def print_self(self):
        print("大家好，我是超人，你们都是垃圾。")

#函数
def introduce(temp):
    temp.print_self()
    
dog1=Dog()
dog2=Xiaotq()

introduce(dog1)
introduce(dog2)
