
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def rotate(self, n):
        if n == 0:
            return
        curr = self.head
        counter = 1
        while(counter <n and curr is not None):
            curr = curr.next
            counter += 1
        if curr is None:
            return
        nth = curr
        while(curr.next is not None):
            curr = curr.next
        curr.next = self.head
        self.head = nth.next
        nth.next = None

if __name__=='__main__':
    ll =LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(5)
    print("before rotation")
    ll.print_linked_list()
    print("rotating ll")

    ll.rotate(2)
    print("after rotation")

    ll.print_linked_list()
 