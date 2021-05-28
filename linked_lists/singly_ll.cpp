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
void insert_at_beginning(Node *&head, Node *&last, int value);
void remove(Node *&head, Node *&last);
void display(Node *curr);
void insert_at_pos(Node *&head, Node *&last, int pos, int value);

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
void insert_at_beginning(Node *&head, Node *&last, int value){
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

void insert_at_pos(Node *&head, Node *&last, int pos, int value){
    if(isListEmpty(head)){
        cout<<"linked list is empty\n adding first element\n";
        addFirstElement(head, last, value);
    }
    else{
        Node *temp =  head;
        Node *new_node = new Node();
        new_node->value =value;
        while(pos!=0){
            temp = temp->next;
            pos=pos-1;
        }    
        new_node->next = temp->next;
        temp->next = new_node;
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

    insert_at_beginning(head, last, num1);
    insert_at_beginning(head, last, num2);
    insert_at_beginning(head, last, num3);
    insert_at_beginning(head, last, num4);
    

   
    insert_at_pos(head,last,3,15);

    display(head);

    remove(head, last);

    cout<<"list after removing first element\n";

    display(head);

    //TODO
    //Remove element from middle
    //remove last element

    return 0;
}