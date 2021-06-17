class BST:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
    
    #iterative
    def insert(self,value):
        curr=self
        while True:
            if curr.value>value:
                if curr.left is None:
                    curr.left= BST(value)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
                    break
                else:
                    curr=curr.right
        return self
    
    #iterative
    def search(self, value):
        curr=self
        while curr is not None:
            if curr.value>value:
                curr = curr.left
            elif curr.value<value:
                curr = curr.right
            else:
                return True
        return False

    #recursive
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()

    #TODO
    #remove

if __name__ == '__main__':
    node= BST(2)
    node.insert(5)
    node.insert(3)
    node.PrintTree()


