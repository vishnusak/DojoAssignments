from SingleLL import Node, SLL

myList = SLL()

myList.add(452)
myList.add(510)
myList.add(412)
myList.add(242)
myList.add(432)
myList.add(425)
myList.add(310)
myList.add(565)
myList.add(513)

myList.attach(3, 142)
myList.attach(13, 3, 'before')
myList.attach(0, 10, 'before')
myList.attach(37, 600, 'before')
myList.attach(40, 42, 'after')
print("The linked list is: {}").format(myList.show())
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)

myResult = myList.sec_to_last()
print("The second to last element is {}").format(myResult)

myList.filter(100, 600)
print("The linked list after filtering is: {}").format(myList.show())
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)

myList.remNode(513)
print("The linked list after filtering is: {}").format(myList.show())
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
