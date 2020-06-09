Node* insert(Node* root,int data){
    if(root==0){
        root=new Node(data);
        return root;}
    if(root->data>=data)
    root->left=insert(root->left,data);
    if(root->data<data)
    root->right=insert(root->right,data);
    return root;
}

Node* constructBst(int arr[], int n)
{
    Node* root=0;
    for(int i=0;i<n;i++){
      root=  insert(root,arr[i]);
    }
    return root;
}