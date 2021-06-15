## BST - Binary Search Tree
class BST:
    def __init__(self, value):
        '''init left node, right node and value'''
        self.left = None
        self.right = None
        self.value = value

# BST Functions in Python
# BST Construction using Inorder Traversal

# constructTreeHelper.Index is a static variable of it's corresponding function

# Get the value of index
def getIndex():
    return constructTreeHelper.Index
 
# Increment the value of index
def incrementIndex():
    constructTreeHelper.Index += 1
 
# A recurseive helper function to construct tree from arr[].
def constructTreeHelper(arr, low, high):
    # Base Case
    if(low > high):
        return None
 
    # Make starting value in arr[] the root
    # Then increment the index
    root = BST(arr[getIndex()])
    incrementIndex()
 
    # Check to see if subarray has only one element
    if low == high:
        return root
 
    temp_root = -1
 
    # Search for the first element greater than root
    for i in range(low, high+1):
        if (arr[i] > root.value):
            temp_root = i
            break
 
    # If no elements are greater than the current root,
    # all elements are on left side of the root
    if temp_root == -1:
        temp_root = getIndex() + (high - low)
 
    # Use the index of element found in arr[] to divide
    # preorder array into left and right subtree
    root.left = constructTreeHelper(arr, getIndex(), temp_root-1)
 
    root.right = constructTreeHelper(arr, temp_root, high)
 
    return root
 
# The main function to construct BST from given preorder traversal
def constructTree(arr):
    size = len(arr)
    constructTreeHelper.Index = 0
    return constructTreeHelper(arr, 0, size-1)
 
# A utility function to print inorder traversal of a Binary Tree
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print (root.value, end=" ")
    printInorder(root.right)
