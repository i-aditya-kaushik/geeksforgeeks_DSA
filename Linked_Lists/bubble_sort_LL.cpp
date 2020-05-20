void swap(struct Node *a, struct Node *b) 
{ 
    int temp = a->data; 
    a->data = b->data; 
    b->data = temp; 
} 

/* Function to bubble the linked list
   It should return head of the modified list  */
Node* bubblesort(Node* head) {
    int swapped, i; 
    struct Node *temp; 
    struct Node *prev = NULL; 
  
    if (head == NULL) 
        return head; 
  
    do
    { 
        swapped = 0; 
        temp = head; 
  
        while (temp->next != prev) 
        { 
            if (temp->data > temp->next->data) 
            {  
                swap(temp, temp->next); 
                swapped = 1; 
            } 
            temp = temp->next; 
        } 
        prev = temp; 
    } while (swapped);
    return(head);
}
