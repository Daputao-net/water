class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """添加一个新的元素item到队尾"""
        self.__list.append(item)

    def dequeue(self):
        """从队头删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())