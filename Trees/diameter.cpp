int dia(Node* root,int &h){
    if(root==NULL){
    h=0;
    return 0;
    }
    int h1,h2;
    int d1=dia(root->left,h1),d2=dia(root->right,h2);
    h=1+max(h1,h2);
    int x=max(d1,d2);
    return max(1+h1+h2,x);
}
/* Computes the diameter of binary tree with given root.  */
int diameter(Node* node) {
  if(node==NULL)
    return 0;
    int h1,h2;
    int d1=dia(node->left,h1),d2=dia(node->right,h2);
    int x=max(d1,d2);
    return max(x,h1+h2+1);
}