from random import random
from queue import Que

myQ = Que()

for i in range(0, 10):
    rand = int(random() * 100)
    print("input is {}").format(rand)
    myQ.enque(rand)

for i in range(0, 10):
    print("Output is {}").format(myQ.deque().data)
