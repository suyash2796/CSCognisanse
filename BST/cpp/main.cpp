#include "bst_construction.cpp"
#include<iostream>
#include<vector>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int arr[] = { 10, 5, 1, 7, 40, 50 };
    int size = sizeof(arr) / sizeof(arr[0]);
 
    BST* root = constructTree(arr, size);
 
    cout << "Inorder traversal of constructed BST: \n";
    printInorder(root);
 
    return 0;
}
