def w1(func):
    def inner():
        print("---正在验证权限----")
        if False:
            func()
        else:
            print("没有权限")
    return inner

#f1 = w1(f1)  @w1就相当于这就这句。 装饰器的原理就是利用闭包将闭包内的函数引用返回去替代原来f1的引用来调用执行f1。
@w1
def f1():
    print("---f1---")

@w1
def f2():
    print("---f2---")

f1()
f2()
