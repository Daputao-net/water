# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        count=len(s)
        for i in range(0,count):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)


if __name__ == "__main__":
    s = Solution()
    src_string = input()
    new_string = s.replaceSpace(src_string)
    print(new_string)