Node *tail=NULL; 

// function inserts the data in front of the list
Node *insertAtBegining(Node *head, int newData) {
   Node* new_node=new Node(newData);
   new_node->next=head;
  if(head==NULL){
  tail=new_node;
  }
   head=new_node;
   return head;
}


// function appends the data at the end of the list
Node *insertAtEnd(Node *head, int newData)  {
   Node* new_node=new Node(newData);
    if(head==NULL){
        head=new_node;
        tail=new_node;
        return head;
    }
   tail->next=new_node;
   tail=tail->next;
   return head;
}