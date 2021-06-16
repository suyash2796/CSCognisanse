#include "bst_construction.cpp"
#include<iostream>
#include<vector>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int arr[] = { 24, 8, 3, 14, 34, 87, 45, 23, 76, 23, 2, 5, 8 };
    int size = sizeof(arr) / sizeof(arr[0]);
 
    BST* root = constructTree(arr, size);
 
    cout << "Inorder traversal of constructed BST: \n";
    printInorder(root);
 
    return 0;
}
