int balanced(Node* root){
    if(root==NULL){
        return(0);
    }
    int lh = balanced(root->left);
    if(lh==-1){
        return(-1);
    }
    int rh = balanced(root->right);
    if(rh==-1){
        return(-1);
    }
    if(abs(lh-rh)>1){
        return(-1);
    }
    return(max(lh,rh)+1);
}

bool isBalanced(Node *root)
{
    int m = balanced(root);
    if(m==-1){
        return(0);
    }
    else{
        return(1);
    }
}s