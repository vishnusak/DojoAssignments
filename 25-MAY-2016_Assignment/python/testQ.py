from queue import Que

values1 = [34, 15, 97, 11, 14, 20, 55, 90, 71, 3]
values2 = [22, 20, 15, 9, 16, 5, 67, 59, 77, 36]

myQ1 = Que()
myQ2 = Que()

for i in values1:
    myQ1.enque(i)

for i in values1:
    myQ2.enque(i)

print("\nQ1 is {}").format(myQ1.show())
print("\nQ2 is {}").format(myQ2.show())

def compareQ(q1, q2):
    q1data = q1.show()
    q2data = q2.show()

    return (q1data == q2data)

print("\nQ1 and Q2 are equal - {}").format(compareQ(myQ1, myQ2))
print("-"*50)

values = [22, 8, 15, 9, 16, 5, 67, 59, 77, 36, 5]
myQ = Que()

for i in values:
    myQ.enque(i)

print("\nQueue is {}").format(myQ.show())

def remMin(q):
    qdata = q.show()
    min = qdata[0]

    for i in range(len(qdata)):
        q.deque()

    for i in qdata:
        min = (i if min > i else min)

    while(min in qdata):
        qdata.remove(min)

    for i in qdata:
        q.enque(i)

remMin(myQ)
print("Queue afer removing min is {}").format(myQ.show())

def interleave(q):
    qdata = q.show()
    newq = []

    mid = ((len(qdata) / 2) +(len(qdata) % 2))
    qdata1 = qdata[0:mid]
    qdata2 = qdata[mid:]

    for i in range(len(qdata)):
        q.deque()

    for i in range(len(qdata1)):
        newq.append(qdata1[i])
        if i<len(qdata2):
            newq.append(qdata2[i])

    for i in newq:
        q.enque(i)

interleave(myQ)
print("Queue afer interleaving is {}").format(myQ.show())
