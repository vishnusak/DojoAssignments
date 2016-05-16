# Single linked list - using functions:

# Making a node
def makenode(data, link=None):
    node_obj = {'data':data, 'link':link}
    return node_obj

# Addtolist - will add new node to end of list
def addtolist(llist, node):
    if not llist:
        llist = node
    else:
        temp = llist
        while (temp['link'] != None):
            temp = temp['link']
        temp['link'] = node

    return llist

# Addtofront - will add new node to front of list
def addtofront(llist, node):
    if not llist:
        llist = node
    else:
        node['link'] = llist
        llist = node

    return llist
#
# Insertitem - inserts the node based on asc order. Assumes a sorted list
# --- currently inserting node. ideally, we should only receive data to insert.
# --- creating a node and inserting it should be handled inside the function
def insertitem(llist, node):
    if not llist:
        llist = node
    else:
        curnode = llist
        prevnode = None
        while((curnode['data'] <= node['data']) and (curnode['link'])):
            prevnode = curnode
            curnode = curnode['link']

        if (curnode['data'] > node['data']):
            node['link'] = curnode
            prevnode['link'] = node
        else:
            curnode['link'] = node

    return llist
#
# Displaylist - displays the data held by the list
def displaylist(llist):
    temp = llist
    print temp['data'],
    while (temp['link']):
        temp = temp['link']
        print temp['data'],
    else:
        print ""
#
# Removeitem - removes a node from the list
# assumption is that this is not an empty list
def removeitem(llist, val):
    cur = llist
    prev = None
    while ((cur['data'] != val) and (cur['link'])):
        prev = cur
        cur = cur['link']

    if (cur['data'] == val):
        if prev:
            prev['link'] = cur['link']
        else:
            llist = cur['link']

    return llist

mylist = None
mynode = makenode(16)
mylist = addtolist(mylist, mynode)
print("After adding 16: {}").format(mylist)
displaylist(mylist)

mynode = makenode(32)
mylist = addtolist(mylist, mynode)
print("After adding 32: {}").format(mylist)
displaylist(mylist)
#
mynode = makenode(8)
mylist = addtofront(mylist, mynode)
print("After adding 8 to the front: {}").format(mylist)
displaylist(mylist)
#
mynode = makenode(24)
mylist = insertitem(mylist, mynode)
print("After inserting 24: {}").format(mylist)
displaylist(mylist)
#
mynode = makenode(64)
mylist = insertitem(mylist, mynode)
print("After inserting 64: {}").format(mylist)
displaylist(mylist)
#
print("The contents of the list are:")
displaylist(mylist)
#
mylist = removeitem(mylist, 24)
print("After removing 24: {}").format(mylist)
displaylist(mylist)
#
mylist = removeitem(mylist, 34)
print("After removing 34: {}").format(mylist)
displaylist(mylist)
#
mylist = removeitem(mylist, 8)
print("After removing 8: {}").format(mylist)
displaylist(mylist)
