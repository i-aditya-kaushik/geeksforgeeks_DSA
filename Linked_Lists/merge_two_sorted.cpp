Node* sortedMerge(Node* head1,   Node* head2)
{
    Node* node = NULL;  
    if (head1 == NULL)  
        return(head2);  
    else if (head2 == NULL)  
        return(head1);  
      
    if (head1->data <= head2->data)  
    {  
        node = head1;  
        node->next = sortedMerge(head1->next, head2);  
    }  
    else
    {  
        node = head2;  
        node->next = sortedMerge(head1, head2->next);  
    }  
    return(node);  
}