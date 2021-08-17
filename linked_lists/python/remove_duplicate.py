class Node:
    def __init__(self,value=None, next=None):
        self.next =next
        self.value = value

class LinkedList:
    
    def __init__(self):  
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def print_linked_list(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next

class solution:
    def remove_dup(self, ll):
        curr = ll
        while curr is not None:
            next_node = curr.next
            while next_node is not None and curr.value==next_node.value:
                next_node =next_node.next
            curr.next = next_node
            curr=next_node
        return ll



if __name__ == '__main__':
    LL = LinkedList()
    LL.insert(3)
    LL.insert(3)
    LL.insert(5)
    LL.insert(5)
    LL.insert(5)
    LL.insert(6)
    print('linked list with duplicates. Linked list is sorted by node values')
    LL.print_linked_list()
    sol = solution()
    #remove duplicates 
    new = sol.remove_dup(LL.head)
    print("new linked list after removing duplicates")
    current = new
    while(current):
        print(current.value)
        current = current.next
