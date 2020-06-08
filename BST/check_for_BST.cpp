bool CHECK(Node *root,int mini,int max)
{
    if(root==NULL)
      return 1;
    if(root->data <= mini || root->data>max)
      return 0;
    return CHECK(root->left,mini,root->data) && CHECK(root->right,root->data,max);
    
}
bool isBST(Node* root) 
{
    // Your code here
    if(root==NULL)
      return 1;
    if(CHECK(root,INT_MIN,INT_MAX))
       return 1;
    else
       return 0;
}