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

# splitList = myList.splitOnVal(0)
# print("\nThe original linked list is: {}").format(myList.show())
# print("Length of original linked list is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
# print("\nThe split linked list is: {}").format(splitList.show())
# print("Length of split linked list is {} - Min is {} - Max is {} - Sum is {}").format(splitList.len, splitList.min, splitList.max, splitList.sum)

myResult = myList.partition(60)
if not myResult:
    print("The linked list is: {}").format(myList.show())
    print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
else:
    print("{}").format(myResult)
