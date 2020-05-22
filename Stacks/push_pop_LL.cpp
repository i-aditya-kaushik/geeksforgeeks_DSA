void MyStack ::push(int x) {
    StackNode* temp=new StackNode(x);
    temp->next=top;
    top=temp;
}

/* The method pop which return the element
  poped out of the stack*/
int MyStack ::pop() {
    struct StackNode* temp; 
    if (top == NULL) { 
        return(-1);
    } 
    else{ 
        StackNode* temp=top;
    top=top->next;
    int data=temp->data;
    free(temp);
    return data;
    }
}