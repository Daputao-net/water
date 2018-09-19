def check(ls, rs, num, n):
    l_num = num[:n]
    r_num = num[n:]
    l_result = conversion_num(l_num, int(ls))
    r_result = conversion_num(r_num, int(rs))

    while l_result < r_result:
        n += 1
        l_num = num[:n]
        r_num = num[n:]
        l_result = conversion_num(l_num, int(ls))
        r_result = conversion_num(r_num, int(rs))

    # if l_result >= r_result:
    #     return r_result
    #
    # elif l_result <= r_result:
    #     check(ls, rs, num, n)
    return r_result

# 将src进制的字符串转化为dest进制
def conversion_num(num, src):
    rtn = ''
    # 1、校验源（N进制）和目标（M进制）是否相同
    if src == 10:
        rtn = num
    # 2、转成10进制#
    if src != 10:
        num_str = num
        # 将列表翻转
        num_str = num_str[::-1]
        exe_num = 0
        dec_num = 0
        # 从最后一位数开始
        for num_char in num_str:
            # 十六进制处理
            if num_char == 'A':
                num_char = '10'
            elif num_char == 'B':
                num_char = '11'
            elif num_char == 'C':
                num_char = '12'
            elif num_char == 'D':
                num_char = '13'
            elif num_char == 'E':
                num_char = '14'
            elif num_char == 'F':
                num_char = '15'

            num_int = int(num_char)
            if exe_num == 0:
                dec_num += num_int
            else:
                dec_num += (src ** exe_num) * num_int
            exe_num += 1
        # 得到给定数字的十进制形式
        rtn = dec_num

    # 3、处理空的字符串
    if rtn == '':
        rtn = '0'
    return rtn


def main():
    # 有t个样例
    t = int(input())
    demo = []
    new = []
    for i in range(t):
        demo.append(input())
        new.append(demo[i].split())
    for i in range(t):
        result = check(new[i][0], new[i][1], new[i][2], n=1)
        print(result)


if __name__ == '__main__':
    main()




