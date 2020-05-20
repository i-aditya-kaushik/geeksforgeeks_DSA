bool isPalindrome(Node *head)
{
    list<int> s1,s2;
    Node* temp = head;
    while(temp!=NULL){
        s1.push_back(temp->data);
        s2.push_front(temp->data);
        temp = temp->next;
    }
    return(s1==s2);
    
}