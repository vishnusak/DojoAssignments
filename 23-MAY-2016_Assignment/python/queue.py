class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Que(object):
    def __init__(self):
        self.__head = None
        self.__tail = None

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
