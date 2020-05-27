int isSumProperty(Node *root)
{
    if(root==NULL) return 1;
    if(root->right==NULL and root->left==NULL){
        return 1;
    }
    int sum = 0;
    if(root->left!=NULL){
        sum+=root->left->data;
    }
    if(root->right!=NULL){
        sum+=root->right->data;
    }
    if(sum==root->data and isSumProperty(root->right)==1 and isSumProperty(root->left)==1){
        return(1);
    }
}