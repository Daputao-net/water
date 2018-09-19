# # 题目描述
# # 输入行和列，生成一个从上到下，从左到右都递增的二维数组
# # 查找一个值在不在数组里面
#
#
# def create_list(n_row, n_column):
#     """自动生成一个二维矩阵"""
#     array = [[] for i in range(n_row)]
#     for i in range(n_column):
#         for j in range(n_row):
#             array[j].append(j+i)
#     return array
#
#
# def input_list():
#     """手动输入一个二维矩阵"""
#     array = []
#     while True:
#         src_str = input()
#         row_list = src_str.split()
#         if len(row_list) == 1:
#             return array, row_list
#         array.append(row_list)
#
#
# def input_array():
#     """手动输入一个二维数组"""
#     src_str = input()
#     array = eval(src_str)
#     return array
#
#
# def check(array, x):
#     total = 0
#     for i in array:
#         num = i.count(x)
#         total += num
#     print(total)
#     if total > 0:
#         return True
#     else:
#         return False
#
#
# if __name__ == "__main__":
#     # n_row = int(input())
#     # n_column = int(input())
#     x = int(input())
#     # array = create_list(n_row, n_column)
#     # array, x = input_list()
#     array = input_array()
#     result = check(array, x)
#     # print(x)
#     # print(array)
#     print(result)

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        n = len(array) - 1
        for i in range(n, -1, -1):
            num = array[i].count(target)
            if num > 0:
                return True
        else:
            return False

    def input_array():
        """手动输入一个二维数组"""
        src_str = input()
        array = eval(src_str)
        return array


if __name__ == "__main__":
    s = Solution()
    target = int(raw_input())
    array = s.input_array()
    result = s.Find(target, array)