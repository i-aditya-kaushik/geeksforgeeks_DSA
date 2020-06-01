Node* findmin(Node* root){
    while(root->left != NULL){
        root = root->left;
    }
    
    return root;
}

Node *deleteNode(Node *root,  int x)
{
    if (root == NULL) return NULL;

    if (x > root->data) {
        root->right = deleteNode(root->right, x);
    }else if (x < root->data) {
        root->left = deleteNode(root->left, x);
    }
    else {
        if(root->left == NULL && root->right == NULL){
            delete root; root = NULL;
        }   
        
        else if(root->left == NULL){
            Node *temp = root;
            root = root->right;
            delete temp;
        }
        else if(root->right == NULL){
            Node* temp = root;
            root = root->left;
            delete temp;
        }
        
        else{
            Node *temp = findmin(root->right);
            root->data = temp->data;
            root->right = deleteNode(root->right, temp->data);
        }
    }
return root;
}