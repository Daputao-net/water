class Node(object):
    """定义一个节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        # 因为不需要让用户知道我的头结点在哪里所以head定义为私有的属性。
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表的长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    # pos/position:位置，方位 param:参数
    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始(即将链表的第一个节点记为0节点)"""
        # pre/previous以前的，在什么之前
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        pre = self.__head

        # 判断是不是空链表
        if pre == None:
            return False
        # 判断是不是头结点，包含了只有一个节点情况
        elif pre.elem == item:
            self.__head = pre.next
            # pre = None
            return True
        else:
            while pre.next != None:
                if pre.next.elem == item:
                    pre.next = pre.next.next
                    return True
                else:
                    pre = pre.next
            return False
        # 也可以使用这种方法
        # cur = self.__head
        # pre = None
        # while cur != None:
        #     if cur.elem == item:
        #         # 先判断此结点是否是头节点
        #         # 头节点
        #         if cur == self.__head:
        #             self.__head = cur.next
        #         else:
        #             pre.next = cur.next
        #         break
        #     else:
        #         pre = cur
        #         cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head

        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    sll = SingleLinkList()

    print(sll.remove(4))
    sll.travel()
    print("----------")
    sll.append(2)
    print(sll.search(2))
    print(sll.remove(2))
    print("----------")
    sll.append(2)
    sll.append(3)
    sll.append(5)
    sll.append(6)
    sll.append(7)
    sll.travel()
    sll.add(1)
    sll.travel()
    sll.insert(3, 4)
    sll.travel()
    sll.remove(1)
    sll.travel()
    sll.remove(7)
    sll.travel()
    sll.remove(4)
    sll.travel()
    print(sll.remove(100))
    sll.travel()
    print(sll.search(6))