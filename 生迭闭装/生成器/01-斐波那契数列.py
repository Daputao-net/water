#num=int(input("请输入要打印的长度:"))

def creatNum():
    print("---start---")
    a,b=0,1
    for i in range(5):
        print("---1---")
        #print(b)
        yield b
        print("---2---")
        a,b=b,a+b
        print("---3---")
    print("---end---")
a=creatNum()

for i in a:
    print(i)
