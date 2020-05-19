void deleteNode(Node *node)
{
   if (node == NULL) // If linked list is empty 
        return; 
    else { 
        if (node->next == NULL) { 
            return; 
        } 
        Node* temp = node->next; 
        node->data = node->next->data; 
        node->next = node->next->next; 
  
        free(temp); 
    } 
}