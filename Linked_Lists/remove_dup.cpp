Node *removeDuplicates(Node *root)
{
    Node* current = root;
    Node * temp;
    while (current != NULL && current->next != NULL)
    {
       if (current->data == current->next->data)
       {
           temp = current->next->next;
           current->next = temp;
       }
       else
       {
          current = current->next;
       }  
    }
    return root;
}