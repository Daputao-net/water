

def binary_search(alist, item):
    """二分法查找_递归"""
    n = len(alist)
    if n > 0:
        mid = (n-1) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    else:
        return False


def binary_search_2(alist, item):
    """二分法查找_非递归"""
    n = len(alist)
    last = n - 1
    first = 0
    while first <= last:
        mid = (first + last) // 2
        # 找到alist[i]要插入的位置
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid-1
        else:
            first = mid+1
    return False


if __name__ == "__main__":
    li = [i for i in range(20)]
    print(li)
    print(binary_search(li, 18))
    print(binary_search_2(li, 16))