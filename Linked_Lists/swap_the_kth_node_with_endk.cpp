Node *swapkthnode(Node* head, int num, int k)
{
    if(k>num)
    return head;
    else
    {
        Node *start_prev=NULL;
        Node *start=head;
        Node *end_prev=NULL;
        Node *end=head;
        for(int i=1;i<k;++i)
        {
            start_prev=start;
            start=start->next;
        }
        for(int i=1;i<num-k+1;++i)
        {
            end_prev=end;
            end=end->next;
        }
        if(start_prev)
            start_prev->next=end;
        if(end_prev)
            end_prev->next=start;
        Node *temp=start->next;
        start->next=end->next;
        end->next=temp;
        if(k==1)
            head=end;
        if(k==num)
            head=start;
        return head;
    }
}