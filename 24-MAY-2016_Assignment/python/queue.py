class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Que(object):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def front(self):
        if(self.__head):
            return self.__head.data
        else:
            return None

    def contains(self, data):
        result = False
        if (self.__head):
            if isinstance(data, Node):
                data = data.data
            cur = self.__head
            while (cur):
                if cur.data == data:
                    result = True
                    break
                else:
                    cur = cur.next

        return result

    def isEmpty(self):
        return (not self.__head)

    def size(self):
        size = 0
        if (self.__head):
            cur = self.__head
            while (cur):
                size += 1
                cur = cur.next

        return size

    def enque(self, data):
        if isinstance(data, Node):
            node = data
        else:
            node = Node(data)

        if self.__tail:
            self.__tail.next = node
        else:
            self.__head = node

        self.__tail = node

    def deque(self):
        result = None

        if self.__head:
            result = self.__head
            self.__head = self.__head.next
        else:
            result = "Empty List"

        return result
