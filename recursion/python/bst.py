class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 
  
   
def inorder(root): 
  
    if root: 
  
        inorder(root.left) 
  
        print(root.data)
  
        inorder(root.right) 
  
  
  
def postorder(root): 
  
    if root: 
  
        postorder(root.left) 
  
        postorder(root.right) 
   
        print(root.data)
  
  
def preorder(root): 
  
    if root: 
   
        print(root.data), 
  
        preorder(root.left) 
  
        preorder(root.right) 
  
  
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
preorder(root) 
  
inorder(root) 
  
postorder(root)