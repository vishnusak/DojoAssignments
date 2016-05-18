from SingleLL import Node, SLL

myList = SLL()

myList.add(42)
myList.add(142)
myList.add(242)
myList.add(432)
myList.add(425)

print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.addFront(0)
myList.addFront(10)
myList.addFront(565)
myList.addFront(13)

print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.remove(0)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.remove(10)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.remove(565)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.remove(13)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.remove(242)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.remove(425)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.remove(42)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.remove(142)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.remove(432)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.remove(10)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.insert(0)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.insert(-1)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.insert(10)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.insert(5)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.insert(4)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.insert(9)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())

myList.insert(11)
print("Length is {} - Min is {} - Max is {} - Sum is {}").format(myList.len, myList.min, myList.max, myList.sum)
print("The List is {}").format(myList.show())
