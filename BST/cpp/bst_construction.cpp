#include<iostream>
#include<vector>
#include <bits/stdc++.h>
using namespace std;

class BST {
    public:
        BST *left;
        BST *right;
        int value ;
};

// BST Functions in C++

// Util. function to create a node
BST* new_node(int value) {
    BST* temp = new BST();
    temp->value = value;
    temp->left = temp->right = NULL;
    return temp;
}
 
// A recursive helper function to construct tree from arr[].
BST* constructTreeHelper(int arr[], int* index, int low, int high, int size) {
    // Base case
    if (*index >= size || low > high)
        return NULL;
 
    // Make starting value in arr[] the root
    // Then increment index
    BST* root = new_node(arr[*index]);
    *index += 1;
 
    // Check to see if subarray has only one element
    if (low == high)
        return root;
 
    // Search for the first element greater than root
    int i;
    for (i = low; i <= high; ++i)
        if (arr[i] > root->value)
            break;
 
    // Use the index of element found in arr[] to divide
    // preorder array into left and right subtree
    root->left = constructTreeHelper(arr, index, *index, i - 1, size);
    root->right = constructTreeHelper(arr, index, i, high, size);
 
    return root;
}
 
// The main function to construct BST from given preorder traversal
BST* constructTree(int arr[], int size) {
    int index = 0;
    return constructTreeHelper(arr, &index, 0, size - 1, size);
}
 
// A utility function to print inorder traversal of a Binary Tree
void printInorder(BST* node) {
    if (node == NULL)
        return;
    printInorder(node->left);
    cout << node->value << " ";
    printInorder(node->right);
}
