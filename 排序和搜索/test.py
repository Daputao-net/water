def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    mid = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    # 退出循环的时候low == high
    alist[low] = mid
    # 对low的左边进行快速排序
    quick_sort(alist, first, low-1)
    # 对low的右边进行快速排序
    quick_sort(alist, low+1, last)


def binary_search(alist, item):
    """二分查找_非递归"""
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


def binary_search_recursive(alist, item):
    """递归查找_递归"""
    n = len(alist)
    if n <= 0:
        return False
    mid = (n-1)//2
    if alist[mid] == item:
        return True
    elif item < alist[mid]:
        return binary_search_recursive(alist[:mid], item)
    else:
        return binary_search_recursive(alist[mid+1:], item)


if __name__ == '__main__':
    li = [56, 45, 33, 22, 96, 79, 88, 64, 9, 16, 8, 21, 25, 28]
    print(*li)
    quick_sort(li, 0, len(li)-1)
    print(*li)
    print(binary_search_recursive(li, 20))
    print(binary_search(li, 21))