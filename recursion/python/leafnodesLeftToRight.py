class newNode:  
      
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None
  
def leafNodes(root): 
      
    if root == None: 
        return
      
    if (root.left == None and 
        root.right == None): 
        print(root.data, end = " ") 
        return
      
    if root.left: 
        leafNodes(root.left) 
      
    if root.right: 
        leafNodes(root.right) 
  
root = newNode(1) 
root.left = newNode(2) 
root.right = newNode(3) 
root.left.left = newNode(4) 
root.left.right = newNode(5) 
root.right.left = newNode(6)
root.right.right = newNode(7)
root.left.left.left = newNode(8) 
root.right.right.left = newNode(9) 
root.left.left.left.right = newNode(10) 

leafNodes(root) 