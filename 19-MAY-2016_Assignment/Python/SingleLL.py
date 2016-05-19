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

    def __updAttr(self):
        """
        method to keep track of the attributes of the list
        """
        self.len = (1 if self.__head else 0)
        self.min = (self.__head.data if self.__head else None)
        self.max = (self.__head.data if self.__head else None)
        self.sum = (self.__head.data if self.__head else None)

        temp = (self.__head.next if self.__head else None)
        while (temp != None):
            self.len += 1
            self.min = (temp.data if (temp.data < self.min) else self.min)
            self.max = (temp.data if (temp.data > self.max) else self.max)
            self.sum += temp.data
            temp = temp.next

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
        if isinstance(data, Node):
            node = data
        else:
            node = Node(data)

        if self.__head:
            cur = self.__head
            while (cur.next != None):
                cur = cur.next
            else:
                cur.next = node
        else:
            self.__head = node

        self.__updAttr()

    def addFront(self, data):
        """
        method to add a new node to the beginning of the list.
        this will also keep the attributes updated
        """
        if isinstance(data, Node):
            node = data
        else:
            node = Node(data)

        if self.__head:
            node.next = self.__head
            self.__head = node
        else:
            self.__head = node

        self.__updAttr()

    def insert(self, data):
        """
        method to insert a new node into the list. This assumes the list to be sorted in ascending.
        this will also keep the attributes updated
        """
        if isinstance(data, Node):
            node = data
        else:
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

        self.__updAttr()

    def remove(self, data):
        """
        method to remove a data node from the list.
        this will also keep the attributes updated
        """
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

        self.__updAttr()

    def min_to_front(self):
        """
        method to move the minimum data node to the head of the list
        """
        if not self.__head:
            return "Empty Linked List"

        if not self.__head.next:
            return "Only 1 node in linked list"

        min = self.__head
        min_prev = None

        cur = self.__head.next
        prev = self.__head

        while (cur != None):
            if (min.data > cur.data):
                min = cur
                min_prev = prev
            prev = cur
            cur = cur.next
        else:
            if (min_prev == None):
                return "Minimum value is already in the front"
            else:
                if (min.next == None):
                    min_prev.next = None
                else:
                    min_prev.next = min.next
                min.next = self.__head
                self.__head = min

    def attach(self, data, exist_data, pos='after'):
        """
        method to insert a new node into the list. Insertion will happen either after or before the 'exist_data' node. 'pos' will tell whether insertion should happen before or after. If exist_data doesn't exist in the list, node is added to the end
        """
        if isinstance(data, Node):
            node = data
        else:
            node = Node(data)

        if not self.__head:
            self.__head = node
        else:
            cur = self.__head
            prev = None

            while ((cur.data != exist_data) and (cur.next != None)):
                prev = cur
                cur = cur.next
            else:
                if (cur.data == exist_data):
                    if (pos == 'after'):
                        if cur.next:
                            node.next = cur.next
                        cur.next = node
                    else:
                        if prev:
                            node.next = cur
                            prev.next = node
                        else:
                            node.next = self.__head
                            self.__head = node
                else:
                    cur.next = node

        self.__updAttr()

    def splitOnVal(self, dataval):
        """
        method to split the existing list into two based on dataval. A new list is returned starting with dataval
        """
        result = None

        if not self.__head:
            result = "Empty Linked List"
        else:
            cur = self.__head
            prev = None

            while((cur.data != dataval) and (cur.next != None)):
                prev = cur
                cur = cur.next

            if not prev:
                self.__head = None
                result = SLL()
                result.add(cur)
            elif ((cur.next == None) and (cur.data != dataval)):
                result = "{} not in linked list".format(dataval)
            else:
                prev.next = None
                result = SLL()
                result.add(cur)

        self.__updAttr()
        return result

    def partition(self, dataval):
        """
        method partitions the existing list by moveing all values lower than dataval to the left of dataval and all higher values to the right
        """
        result = None

        if not self.__head:
            result = "Empty Linked List"
        else:
            cur = self.__head
            prev = None

            while ((cur.data != dataval) and (cur.next != None)):
                prev = cur
                cur = cur.next

            if ((cur.next == None) and (cur.data != dataval)):
                result = "{} not in linked list".format(dataval)
            elif (prev != None):
                prev.next = cur.next
                cur.next = self.__head
                self.__head = cur

        if (not result):
            cur = self.__head.next
            prev = self.__head

            while (cur != None):
                if (cur.data <= dataval):
                    prev.next = cur.next
                    cur.next = self.__head
                    self.__head = cur
                    cur = prev.next
                else:
                    prev = cur
                    cur = cur.next

        return result
