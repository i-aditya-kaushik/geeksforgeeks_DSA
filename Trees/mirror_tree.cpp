void mirror(Node* node) 
{
    if(node==NULL){
        return;
    }
    if(node->left and node->right){
        Node* temp = node->right;
        node->right = node->left;
        node->left = temp;
    }
    else if(!node->left and node->right){
        node->left=node->right;
        node->right=NULL;
    }
    else if(!node->right and node->left){
        node->right=node->left;
        node->left=NULL;
    }
    mirror(node->left);
    mirror(node->right);
}