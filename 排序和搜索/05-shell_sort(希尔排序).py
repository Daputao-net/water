#            希尔排序
# 1.希尔排序是按照不同步长对元素进行插入排序
# 2.当刚开始元素很无序的时候，步长最大，所以插入排序的元素个数很少，速度很快
# 3.当元素基本有序了，步长很小，插入排序对于有序的序列效率很高。
# 4.最优复杂度：O(n^1.3)   最坏复杂度：O(n^2)   稳定性：不稳定

def shell_sort(alist):
    n = len(alist)
    step = n//2

    while step > 0:
        for j in range(step, n):
            for i in range(j, 0, -step):
                if alist[i] < alist[i-step]:
                    alist[i], alist[i-1] = alist[i-1], alist[i]
                else:
                    break
        step = step//2


if __name__ == '__main__':

    li = [56, 26, 77, 6, 54, 38, 96, 43, 99]
    print(*li)
    shell_sort(li)
    print(*li)
