#           归并排序
# 归并排序的思想是先递归分解数组，再合并数组
# 将数组分解最小之后，然后合并两个有序数组。
# 基本思路就是比较两个数组最前面的数，谁小就取谁，
# 取了后相应的指针就往后移一位。
# 然后再比较，直至一个数组为空，最后把两一个数组的剩余部分复制过来即可。
# 最优复杂度：O(nlogn)   最坏复杂度：O(nlogn)   稳定性：稳定
import random


def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    # left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])

    # 将两个有序的子序列合并为一个新的整体
    left, right = 0, 0
    result = []

    while left < len(left_li) and right < len(right_li):
        # print(left_li[left], right_li[right])
        if left_li[left] <= right_li[right]:
            result.append(left_li[left])
            left += 1
        else:
            # right_li[right] < left_li[left]
            result.append(right_li[right])
            right += 1
    result += left_li[left:]
    result += right_li[right:]

    return result


if __name__ == '__main__':
    li = []
    for i in range(10):
        li.append(random.randint(1, 100))
    print(*li)
    result = merge_sort(li)
    print(*result)
