class Node(object):
    """节点"""

    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双向链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # counter:记录数量
        counter = 0
        while cur != None:
            counter += 1
            cur = cur.next
        return counter

    def append(self, item):
        """链表尾部添加节点，尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def add(self, item):
        """链表头部添加节点，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def insert(self, pos, item):
        """任意位置添加节点"""
        # pos的初始值为0
        if pos <= 0:
            self.add()
        elif pos > (self.length()-1):
            self.append()
        else:
            cur = self.__head
            counter = 0
            while counter != pos:
                counter += 1
                cur = cur.next
            node = Node(item)
            node.prev = cur.prev
            cur.prev.next = node
            node.next = cur
            cur.prev = node

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def remove(self, item):
        """根据元素删除节点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next != None:
                    # 链表不只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next != None:
                        cur.next.prev = cur.prev
                return True
            else:
                cur = cur.next
        return False

    def search(self, item):
        """根据元素查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    sll = DoubleLinkList()

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