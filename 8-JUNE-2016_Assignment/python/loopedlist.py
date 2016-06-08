class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None

class sList(object):
    def __init__(self):
        self.__head = None

    def make_loop(self, num_of_nodes, loop_node):
        for i in range(num_of_nodes):
            newnode = Node(10 * (i + 1))

            if not self.__head:
                self.__head = newnode
            else:
                temp = self.__head
                while temp.next:
                    temp = temp.next
                temp.next = newnode

            if (i + 1) == loop_node:
                loop_head = newnode

        try:
            newnode.next = loop_head
        except:
            newnode.next = None

        return self.show_loop(num_of_nodes)

    def show_loop(self, num):
        result = []
        temp = self.__head

        for i in range(num * 2):
            try:
                result.append(temp.val)
                temp = temp.next
            except:
                break

        return result

myLoop = sList()
nodes = 10
loop_start = 1

print("The number of nodes is {}").format(nodes)
print("The place where looping starts is {}").format(loop_start)
print("The looped list is {}").format(myLoop.make_loop(nodes, loop_start))
