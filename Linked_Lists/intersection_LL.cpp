int getcount(Node* head){
    int c =0;
    while(head!=NULL){
        c+=1;
        head = head->next;
    }
    return(c);
}

int intersectPoint(Node* head1, Node* head2)
{
    Node* temp1 = head1;
    Node* temp2 = head2;
    int c1,c2;
    c1 = getcount(temp1);
    c2 = getcount(temp2);
    if(c1-c2>0){
        while(c1!=c2){
            head1 = head1->next;
            c1--;
        }
    }
    if(c1-c2<0){
        while(c1!=c2){
            head2 = head2->next;
            c2--;
        }
    }
    // while(head2!=NULL and head1!=NULL){
    //     cout<<head1-> data<<" "<<head2->data;
    //     cout<<"\n";
    //     head1 = head1->next;
    //     head2 = head2->next;
    // }
    while(head2!=NULL and head1!=NULL){
        //cout<<head1->data<<" "<<head2->data<<endl;
        if(head1 == head2){
            if(head1->next!=NULL){
                if(head1->next==head2->next){
                    return(head1->data);
                }
            }
            if(head1->next==NULL){
                return(head1->data);
            }
        } 
        head1 = head1->next;
        head2 = head2->next;
    }
    return(-1);
}