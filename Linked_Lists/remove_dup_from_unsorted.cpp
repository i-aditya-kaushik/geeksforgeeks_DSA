Node * removeDuplicates( Node *head) 
{
    unordered_set<int>us;
    if(head==NULL||head->next==NULL)
        return head;
    Node* curr=head;
    us.insert(curr->data);
    while(curr->next!=NULL){
        Node*next=curr->next;
        if(us.find(next->data)!=us.end()){
            curr->next=next->next;
            free(next);
        }
        else {
            curr=curr->next;
            us.insert(curr->data);
        }
    }
    return head;
}