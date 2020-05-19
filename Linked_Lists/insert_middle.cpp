Node* insertInMiddle(Node* head, int x)
{
	Node* fast=head;
	Node* slow=head;
	while(fast!=NULL and fast->next!=NULL){
	    if(fast->next->next==NULL){
	        break;
	    }
	    fast = fast->next->next;
	    slow = slow->next;
	}
	Node* temp = new Node(x);
	temp->next = slow->next;
	slow->next = temp;
	return head;
}