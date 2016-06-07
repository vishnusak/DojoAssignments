import random as rnd

class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None

class sList(object):
    def __init__(self):
        self.__head = None
        self.__len = 0

    def show(self):
        if (self.__head):
            thisList = []
            temp = self.__head
            while temp:
                thisList.append(temp.val)
                temp = temp.next
            return thisList
        else:
            return None

    def valueAt(self, pos):
        if (pos > self.__len) or (pos < 1):
            return None
        elif not self.__head:
            return None
        else:
            temp = self.__head
            for i in range(1, pos):
                temp = temp.next
            return temp.val

    def len(self):
        return self.__len

    def add(self, val):
        newnode = Node(val)

        if self.__head:
            temp = self.__head
            while (temp.next):
                temp = temp.next
            temp.next = newnode
        else:
            self.__head = newnode

        self.__len += 1

myList = sList()

for i in range(1, 11):
    myList.add(rnd.randint(1,20))

print("The list is {}").format(myList.show())
print("The length of the list is {}").format(myList.len())

k_from_last = 6
myResult = myList.valueAt(myList.len() - k_from_last + 1)

if myResult:
    print("The value at the '{}' position from the end of the list is {}").format(k_from_last, myResult)
else:
    print("The position requested - {} - is invalid").format(k_from_last)
