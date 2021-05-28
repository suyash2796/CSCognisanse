#include<iostream>
using namespace std;

//Node struct for LL implementation
struct Node
{
    int value;
    Node *next;
};


bool isListEmpty(Node *head);
void addFirstElement(Node *&head, Node *&last, int value);
void insert(Node *&head, Node *&last, int value);
void remove(Node *&head, Node *&last);
void display(Node *curr);

//checks if list is empty i.e head==NULL
bool isListEmpty(Node *head){
    if (head==NULL)
        return true;
    else
        return false;
}
//adds first element in linked list
void addFirstElement(Node *&head, Node *&last, int value){
    Node *temp = new Node();
    temp->value = value;
    temp->next = NULL;
    head = temp;
    last = temp;
}
//checks if list is empty.
//if yes, then add first element
//if No, then add element in LL
void insert(Node *&head, Node *&last, int value){
    if(isListEmpty(head))
        addFirstElement(head, last, value);
    else{
        Node *temp = new Node();
        temp->value = value;
        temp->next = NULL;
        last->next = temp;
        last=temp;
    }
}

//remove first element from the linked list
void remove(Node *&head, Node *&last){
    if(isListEmpty(head))
        cout<<"List is empty\n";
    else if(head==last){
        delete head;
        head==NULL;
        last==NULL;
    }
    else{
        Node *temp = head;
        head= head->next;
        delete temp;
    }
}

//display linked list elements
void display(Node *curr){
    if(isListEmpty(curr))
        cout<<"linked list is empty\n";
    else{
        cout<<"list below\n";
        while(curr!=NULL){
            cout<<"("<<curr->value<<", "<<curr->next<<")\n";
            curr = curr->next;
        }
    }
}

//Main function
int main(){

    Node* head =  NULL;
    Node* last =  NULL;

    int num1=2;
    int num2=3;
    int num3=4;
    int num4=5;

    insert(head, last, num1);
    insert(head, last, num2);
    insert(head, last, num3);
    insert(head, last, num4);

    display(head);

    remove(head, last);

    cout<<"list after removing first element\n";

    display(head);

    //TODO
    //Add element in middle
    //Remove element from middle
    //remove last element

    return 0;
}