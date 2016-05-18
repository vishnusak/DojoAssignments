# Single Linked List using classes


class Node(object):
    """
    Class for creating a node object.
    This will have just two attributes: data and next.
    This will not have any methods
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL(object):
    """
    Class for creating a single linked list. This will have the following attributes:
    len -> length of the list. For empty list will be 0
    max -> maximum value held in the list. For empty list will be None
    min -> minimum value held in the list. For empty list will be None
    sum -> sum of all values held in the list. For empty list will be None
    """
    def __init__(self):
        self.len = 0
        self.min = None
        self.max = None
        self.sum = None
        self.__head = None

    def __updLen(self, val=1):
        """
        method to keep track of length of list
        """
        self.len += val

    def __updMin(self, data=None):
        """
        method to keep track of minimum value in list. handle case where data is added to the list as well as when data is removed from the list
        """
        if data != None:
            if self.min == None:
                self.min = data
            elif self.min > data:
                self.min = data
        else:
            self.min = (self.__head.data if self.__head else None)
            cur = (self.__head.next if self.__head else None)
            while (cur != None):
                self.min = (cur.data if (cur.data < self.min) else self.min)
                cur = cur.next

    def __updMax(self, data=None):
        """
        method to keep track of maximum value in list. handle case where data is added to the list as well as when data is removed from the list
        """
        if data != None:
            if self.max == None:
                self.max = data
            elif self.max < data:
                self.max = data
        else:
            self.max = (self.__head.data if self.__head else None)
            cur = (self.__head.next if self.__head else None)
            while (cur != None):
                self.max = (cur.data if (cur.data > self.max) else self.max)
                cur = cur.next

    def __updSum(self, data):
        """
        method to keep track of sum of all values in list.
        """
        if self.sum:
            self.sum += data
        else:
            self.sum = data

    def show(self):
        """
        method to display the contents of the list. This will return an array / list of all values. When empty, this will return the string "Empty Linked List"
        """
        if self.__head:
            list_data = []
            cur = self.__head
            while (cur != None):
                list_data.append(cur.data)
                cur = cur.next
            return list_data
        else:
            return "Empty Linked List"

    def add(self, data):
        """
        method to add a new node to the list. This will add the node to the end of the exitsing list.
        this will also keep the attributes updated
        """
        node = Node(data)
        if self.__head:
            cur = self.__head
            while (cur.next != None):
                cur = cur.next
            else:
                cur.next = node
        else:
            self.__head = node

        self.__updLen()
        self.__updMin(data)
        self.__updMax(data)
        self.__updSum(data)

    def addFront(self, data):
        """
        method to add a new node to the beginning of the list.
        this will also keep the attributes updated
        """
        node = Node(data)
        if self.__head:
            node.next = self.__head
            self.__head = node
        else:
            self.__head = node

        self.__updLen()
        self.__updMin(data)
        self.__updMax(data)
        self.__updSum(data)

    def insert(self, data):
        """
        method to insert a new node into the list. This assumes the list to be sorted in ascending.
        this will also keep the attributes updated
        """
        node = Node(data)
        if self.__head:
            cur  = self.__head
            prev = None
            while ((cur.data <= data) and (cur.next != None)):
                prev = cur
                cur  = cur.next
            else:
                if (cur.data <= data):
                    cur.next = node
                elif (prev == None):
                    node.next   = cur
                    self.__head = node
                else:
                    prev.next = node
                    node.next = cur
        else:
            self.__head = node

        self.__updLen()
        self.__updMin(data)
        self.__updMax(data)
        self.__updSum(data)

    def remove(self, data):
        if not self.__head:
            return
            
        cur  = self.__head
        prev = None
        done = False

        while ((cur.data != data) and (cur.next != None)):
            prev = cur
            cur = cur.next
        else:
            if cur.data == data:
                if cur.next == None:
                    if prev:
                        prev.next = None
                        done = True
                    else:
                        self.__head = None
                        done = True
                else:
                    if prev:
                        prev.next = cur.next
                        done = True
                    else:
                        self.__head = cur.next
                        done = True

        if done:
            self.__updLen(-1)
            self.__updMin()
            self.__updMax()
            self.__updSum(-1 * data)
