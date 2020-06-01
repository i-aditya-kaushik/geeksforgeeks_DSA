int minValue(Node* root)
{
    Node* temp = root;
    while(true){
        if(temp->left==NULL){
            return(temp->data);
        }
        temp = temp->left;
    }
}