def main(li, n):

    if len(li) != n:
        return False
    a = []
    b = []
    for i in range(0, n, 2):
        a.append(li[i])
    for i in range(1, n, 2):
        b.append(li[i])
    a_num = 0
    b_num = 0
    for i in a:
        a_num += int(i)
    for i in b:
        b_num += int(i)

    if a_num == b_num:
        print("0")
    elif a_num > b_num:
        print("1")
    else:
        print("2")


if __name__ == '__main__':
    n = int(input())
    s = input()
    li = s.split()
    main(li, n)
