Node* rotate(Node* head, int k) {
    if (k == 0)  
    return head;  
    Node* current = head;  
    int count = 1;  
    while (count < k && current != NULL)  
    {  
        current = current->next;  
        count++;  
    }  
    if (current == NULL)  
        return head;  
    Node* temp = current;  
    while (current->next != NULL)  
        current = current->next;  
    current->next = head;  
    head = temp ->next;  
    temp->next = NULL;  
    return(head);
}