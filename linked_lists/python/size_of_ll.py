class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    
    def add_item(self, data):
        node=Node(data)
        if self.head:
            self.head.next =node
            self.head =node
        else:
            self.head=node
            self.tail=node
        self.count+=1

    def iter_item(self):
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val


if __name__=="__main__":
    items = LinkedList()
    items.add_item('foobar')
    items.add_item('bar')
    items.add_item('foo')
    items.add_item('f00++')
    items.add_item('fobara')

    for val in items.iter_item():
        print(val)

    print("\nSize of the linked list:",items.count)
