class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):

    def __init__(self, head=None):
        '''initialize head with None'''
        self.head = head

    #O(1)
    #insert new Node in front
    def insert_new_node(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    #O(N)
    def get_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    #O(N) - in worst case you have to traverse whole list
    def search_node(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            print("Key not found in List!")
            return 0
        return current

    #O(N) and Leap frogging
    #In worst case it will visit all nodes
    def delete_node(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                #Leap Frogging
                previous = current
                current = current.get_next()
        if current is None:
            print("Key not found in List")
            return 0
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert_new_node(5)
    l1.insert_new_node(10)
    l1.insert_new_node(15)
    #size is 3 here
    print(l1.get_size())
    print(l1.search_node(10))
    #deleted one node
    l1.delete_node(5)
    #size is 2 here
    print(l1.get_size())