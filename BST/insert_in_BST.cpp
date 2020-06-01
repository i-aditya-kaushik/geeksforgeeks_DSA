Node* insert(Node* root, int key)
{
    Node* temp=root;
    while(true){
        // cout<<temp->data<<endl;
        if(temp->data==key){
            return(root);
        }
        if(temp->data<key){
            if(temp->right==NULL){
                temp->right = new Node(key);
                return(root);
            }
            temp = temp->right;
        }
        if(temp->data>key){
            if(temp->left==NULL){
                temp->left = new Node(key);
                return(root);
            }
            temp = temp->left;
        }
    }
}