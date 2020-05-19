int detectloop(Node *head) {
    Node* temp = head;
    Node* fast = head;
    while(temp!=NULL and fast->next!=NULL and fast->next->next!=NULL){
        fast = fast->next->next;
        temp= temp->next;
        if(fast==temp){
            return(1);
        }
    }
    return(0);
}