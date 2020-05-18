int getCount(struct Node* head){
    Node *temp = head;
    int count=0;
    while(temp!=NULL){
        count+=1;
        temp= temp->next;
    }
    return(count);
}