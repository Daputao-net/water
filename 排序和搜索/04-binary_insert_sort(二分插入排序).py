#               插入排序
# ⒈ 从第一个元素开始，该元素可以认为已经被排序
# ⒉ 取出下一个元素，在已经排序的元素序列中从后向前扫描
# ⒊ 如果该元素（已排序）大于新元素，将该元素移到下一位置
# ⒋ 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# ⒌ 将新元素插入到下一位置中
# ⒍ 重复步骤2~5
# 如果比较操作的代价比交换操作大的话，可以采用二分查找法来减少比较操作的数目。
# 该算法可以认为是插入排序的一个变种，称为二分查找排序。
# 最优复杂度：O(n)    最坏复杂度：O(n^2)    稳定性：稳定
import random


def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    # if alist[1] < alist[0]:
    #     alist[1], alist[0] = alist[0], alist[1]

    for i in range(2, n):
        if alist[i] < alist[i-1]:
            high = i - 1
            low = 1
            temp = alist[i]
            while low <= high:
                # 找到alist[i]要插入的位置
                mid = (low + high) // 2

                if low < high and temp < alist[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            count = i-1
            while count+1 != low:

                alist[count+1] = alist[count]
                count -= 1
            alist[low] = temp


if __name__ == '__main__':
    li = []
    for i in range(10):
        li.append(random.randint(1, 100))
    #li = [5, 3, 2, 4, 7, 1, 6]
    #li = [1, 2, 3, 4, 5, 6, 7]
    print(*li)
    # low_time = time.time()
    insert_sort(li)
    # end_time = time.time()
    print(*li)
    # print(end_time-low_time)
    # insert_sort(li)
    # print(*li)
    # insert_sort(li)
    # print(*li)