from SingleLL import Node, SLL

myList = SLL()

myList.add(42)
myList.add(10)
myList.add(142)
myList.add(242)
myList.add(432)
myList.add(425)
myList.add(10)
myList.add(565)
myList.add(13)

print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myResult = myList.min_to_front()
if myResult:
    print("{}").format(myResult)
else:
    print("The List is {}").format(myList.show())

myList.attach(3, 142)
print("The linked list after attaching 3 after 142 is: {}").format(myList.show())

myList.attach(13, 3, 'before')
print("The linked list after attaching 13 before 3 is: {}").format(myList.show())

myList.attach(0, 10, 'before')
print("The linked list after attaching 0 before 10 is: {}").format(myList.show())

myList.attach(37, 600, 'before')
print("The linked list after attaching 37 before 600 is {}").format(myList.show())

myList.attach(40, 42, 'after')
print("The linked list after attaching 40 after 42 is: {}").format(myList.show())
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
