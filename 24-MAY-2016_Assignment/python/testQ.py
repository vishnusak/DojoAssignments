from random import random
from queue import Que

myQ = Que()

for i in range(0, 10):
    rand = int(random() * 100)
    print("input is {}").format(rand)
    myQ.enque(rand)

# for i in range(0, 10):
#     print("Output is {}").format(myQ.deque().data)

print("\nThe size of the queue is {}").format(myQ.size())
print("\nThe front of the queue is {}").format(myQ.front())
print("\nThe queue contains 85 - {}").format(myQ.contains(85))
print("\nThe queue is empty - {}\n").format(myQ.isEmpty())
