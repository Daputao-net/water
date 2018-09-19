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
        num = dec_num
    # # 3、处理空的字符串
    # if rtn == '':
    #     rtn = '0'
    return rtn


result = conversion_num('10', 13)
print(result)