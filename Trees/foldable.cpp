bool tree(Node *l,Node* r)
{
    if(l==NULL && r==NULL)
        return true;
    return (l && r) && tree(l->left,r->right) && tree(l->right,r->left);
}
bool IsFoldable(Node* root)
{
    if(root==NULL){
        return(true);
    }   
    return(tree(root->left,root->right));
}