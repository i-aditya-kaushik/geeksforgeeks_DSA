struct Node* pairwise_swap(struct Node* head)
{
    if(head->next==NULL){
        return(head);
    }
    Node* next = head->next;
    Node* temp = head->next;
    head->next = head->next->next;
    next->next = head;
    head = next;
    if(head->next->next!=NULL)
        head->next->next = pairwise_swap(head->next->next);
    return(temp);
}