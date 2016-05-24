from stack import Stack

values = [34, 15, 97, 11, 14, 20, 55, 90, 71, 3]
myStk = Stack()

for i in values:
    myStk.push(i)

print("The stack is {}").format(myStk.show())
print("The top of the stack is {}").format(myStk.top())
print("The stack contains 20 - {}").format(myStk.contains(20))
print("The stack contains 85 - {}").format(myStk.contains(85))
print("The stack is empty - {}").format(myStk.isEmpty())
print("The size of the stack is {}").format(myStk.size())

for i in range(len(values)):
    print("The popped value is {}").format(myStk.pop().data)
