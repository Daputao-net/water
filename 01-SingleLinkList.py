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
            print(cur.elem)
            cur = cur.next

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
            per = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                per = per.next
            node.next = per.next
            per.next = node

    def remove(self, item):
        """删除节点"""
        per = self.__head
        if per == None:
            return False
        elif per.elem == item:
            self.__head = per.next
            per = None
            return True
        else:
            while per.next != None:
                if per.next.elem == item:
                    per.next = per.next.next
                    return True
                else:
                    per = per.next
            return False


    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head

        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


