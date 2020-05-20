Node* segregate(Node *head) {
    list <int> l1;
    Node* temp = head;
    while(temp!=NULL){
        l1.push_back(temp->data);
        temp = temp->next;
    }
    l1.sort();
    Node* temp2 = head;
    for(int x: l1){
        temp2->data = x;
        temp2 = temp2->next;
    }
    return(head);
}