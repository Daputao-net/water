#                       快速排序
# 通过一趟排序将要排序的数据分割成独立的两部分
# 其中一部分的所有数据都比另外一部分的所有数据都要小
# 然后再按此方法对这两部分数据分别进行快速排序
# 整个排序过程可以递归进行，以此达到整个数据变成有序序列
# 过程描述
# 1.定义一个标杆，将列表的第一个元素存入标杆，列表的第一个位置相当于空出来了
# 2.定义两个指针low,high，分别记录列表头和列表尾的位置
# 3.判断low是不是小于high，列表尾high位置的元素是不是大于等于标杆，如果是high向左移动一位
#   重复执行这步判断，当条件不成立时，让low位置存放当前high位置的元素
# 4.判断low是不是小于high，列表头low位置的元素是不是小于标杆，如果是low向右移动一位
#   重复执行这步判断，当条件不成立时，让high位置存放当前low位置的元素
# 5.让4、5两步交替执行，直到low >= high时退出循环。此时low = high
# 6.此时找到的low的位置就是标杆的位置，将记录的标杆元素，放置在这个位置。
# 7.递归执行上述步骤直到low >= high时退出。
# 8.最优时间复杂度计算：n拆分多少次能只剩一个元素，也就是n除以多少次2能等于1
#   即n/2^x = 1 --> 2^x = n --> x = logn (log以2为底，n的对数)
#   每次让列表中的值沿着初始值分为左右两半的过程的时间复杂度为n
#   所以最优时间复杂度为nlogn
# 9.最优复杂度：O(nlogn)   最坏复杂度：O(n^2)   稳定性：不稳定

def quick_sort(alist, first, last):
    """快速排序"""

    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        # high左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        # low 右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 循环退出low = high
    alist[low] = mid_value
    # 对low左边的进行快速排序
    quick_sort(alist, first, low-1)
    # 对low右边的进行快速排序
    quick_sort(alist, low+1, last)


if __name__ == '__main__':
    li = [8, 7, 10, 9, 12, 11, 14]
    print(*li)
    quick_sort(li, 0, len(li)-1)
    print(*li)