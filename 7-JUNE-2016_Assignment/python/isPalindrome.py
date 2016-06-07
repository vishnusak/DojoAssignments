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

isPalindrome = True
myList = sList()

myList.add('m')
myList.add('a')
myList.add('d')
myList.add('a')
myList.add('m')

print("The list content is '{}'").format(reduce((lambda a,b: a+b),myList.show()))
print("The length of the list is {}").format(myList.len())

j = myList.len()

for i, j in zip(range(1, j+1), range(j, 0, -1)):
    if myList.valueAt(i) != myList.valueAt(j):
        isPalindrome = False
        break

print("The contents of the list make a palindrome - {}").format(isPalindrome)
