class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):
        self.__head = None

    def show(self):
        if (self.__head):
            thisQ = []
            cur = self.__head
            while(cur):
                thisQ.append(cur.data)
                cur = cur.next
            return thisQ
        else:
            return None

    def top(self):
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

    def push(self, data):
        if isinstance(data, Node):
            node = data
        else:
            node = Node(data)

        if self.__head:
            node.next = self.__head

        self.__head = node

    def pop(self):
        result = None

        if self.__head:
            result = self.__head
            self.__head = self.__head.next

        return result
