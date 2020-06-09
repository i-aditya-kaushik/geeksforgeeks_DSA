void myfunc(Node* root, int l, int h, int &m){
    if(!root){
        return;
    }
    if(root->left) myfunc(root->left, l , h ,m);
    if(root->right) myfunc(root->right, l , h ,m);
    if(root->data>=l and root->data<=h){
        m+=1;
    }
}

int getCountOfNode(Node *root, int l, int h)
{
    int m = 0;
    myfunc(root, l, h, m);
    return(m);
}