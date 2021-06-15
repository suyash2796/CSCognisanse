from src.bst_construction import *

arr = [24, 8, 3, 14, 34, 87, 45, 23, 76, 23, 2, 5, 8]
 
root = constructTree(arr)
print "Inorder traversal of constructed BST:"
printInorder(root)
