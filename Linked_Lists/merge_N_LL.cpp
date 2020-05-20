Node * mergeKLists(Node *arr[], int N)
{
    list<int> l1;
    Node* res= new Node(-1);
    Node* temp;
    for(int i=0;i<N;i++){
        Node* temp = arr[i];
        while(temp!=NULL){
            l1.push_back(temp->data);
            temp = temp->next;
        }
    }
    l1.sort();
    for(int x:l1){
        if(res->data == -1){
            res->data = x;
            temp = res;
            continue;
        }
        res->next = new Node(x);
        res = res->next;
    }
    return(temp);
}