#pragma once
#ifndef bst_construction_H
#define bst_construction_H

#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

class BST {
    public:
        BST *left;
        BST *right;
        int value ;
};

BST* new_node(int value);
BST* constructTreeHelper(int arr[], int* index, int low, int high, int size);
BST* constructTree(int arr[], int size);
void printInorder(BST* node);
    
#endif
