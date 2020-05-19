int getNthFromLast(Node *head, int n)
{
    vector<int> s1;
    while(head!=NULL){
        s1.push_back(head->data);
        head=head->next;
    }
    return(n>s1.size()?-1:s1.rbegin()[n-1]);
}