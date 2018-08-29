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


def insert_sort(alist):
    """插入排序"""
    n = len(alist)

    for j in range(1, n):
        # 1~n-1
        for i in range(j, 0, -1):
            # range(start, stop[, step])
            # stop的值要取前一个，所以此处取值为j~1,
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]

            # 此处为对代码的优化
            # 因为序列的alist[i]之前的序列已经是有序的了
            # 如果alist[i] >= alist[i-1]直接放入前面的有序部分的尾部就行
            # 没有必要再和前面的元素依次比较了
            # 此处的优化使代码的最优时间复杂度由O(n^2)变为了O(n)
            else:
                break


if __name__ == '__main__':
    # li = [5, 3, 2, 4, 7, 1, 6]
    li = [1, 2, 3, 4, 5, 4, 6, 7]
    print(*li)
    # start_time = time.time()
    insert_sort(li)
    # end_time = time.time()
    print(*li)
    # print(end_time-start_time)
   