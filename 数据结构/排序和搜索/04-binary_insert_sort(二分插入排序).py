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


def binary_insert(l):
    n = len(l)
    for i in range(1, n):
        if l[i] < l[i-1]:
            low = 0
            high = i-1
            temp = l[i]
            while low <= high:
                mid = (low + high)//2
                if l[i] < l[mid]:
                    high = mid-1
                else:
                    low = mid+1

            count = i
            while count != low:
                l[count] = l[count-1]
                count -= 1
            l[low] = temp


if __name__ == '__main__':
    li = [3, 2, 6, 5, 1, 4]
    # for i in range(100):
    #     li.append(random.randint(0, 1000))
    print(*li)

    binary_insert(li)

    print(*li)
