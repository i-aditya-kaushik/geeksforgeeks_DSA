bool search(Node* root, int x)
{
    Node* temp=root;
    while(true){
        if(temp->data==x){
            return(true);
        }
        if(temp->data<x){
            if(temp->right==NULL){
                return(false);
            }
            temp = temp->right;
        }
        if(temp->data>x){
            if(temp->left==NULL){
                return(false);
            }
            temp=temp->left;
        }
    }
}