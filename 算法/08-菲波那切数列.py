def creatNum(n):
    a, b= 0, 1
    alist = []
    for i in range(n):
        alist.append(b)
        a, b = b, a+b
    print(alist)


def creatNum2(n):
    """生成器版"""
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a+b


def main():
    count = int(input("输入生成数列的长度："))
    for i in creatNum2(count):
        print(i, end=" ")


if __name__ == '__main__':
    main()