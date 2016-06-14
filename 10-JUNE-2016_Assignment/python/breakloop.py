import random as rd

class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None

class sList(object):
    def __init__(self):
        self.__head = None

    def make_loop(self, num_of_nodes, loop_node):
        for i in range(num_of_nodes):
            # newnode = Node(rd.randint(1, 10))
            newnode = Node(10 * (i+1))

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

    def is_loop(self):
        result = False
        node_list = []
        count = 0
        temp = None

        if self.__head:
            node_list.append(self.__head)
            count += 1
            temp = self.__head.next

            while temp:
                if temp in node_list:
                    result = [(node_list.index(temp) + 1), count]
                    break
                else:
                    node_list.append(temp)
                    count += 1
                    temp = temp.next

        return result

    def break_loop(self, num_of_nodes):
        temp = self.__head

        for i in range(1, num_of_nodes):
            temp = temp.next

        temp.next = None

        return self.show_loop(num_of_nodes)

if __name__ == "__main__":
    myLoop = sList()
    nodes = 12
    loop_start = 5

    print("The number of nodes is {}").format(nodes)
    print("The place where looping starts is {}").format(loop_start)
    print("The looped list is {}").format(myLoop.make_loop(nodes, loop_start))

    isLoop = myLoop.is_loop()
    if isLoop:
        print("The list has a loop. The last node is {} and looping starts at node {}").format(isLoop[1], isLoop[0])
        print("The list after breaking the loop is {}").format(myLoop.break_loop(isLoop[1]))
    else:
        print("The list doesn't have a loop")
