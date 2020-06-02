void insertRange(Node* root,int low,int high,vector<int> &s){
    if(root)
    {
        insertRange(root->left,  low, high, s);
        
        if(root->data >= low && root->data <= high)
        {
            s.push_back(root->data);
        }
        
        insertRange(root->right, low, high, s);
    }
}
vector<int> printNearNodes(Node *root, int low, int high)
{
    vector<int> res;
    insertRange(root, low, high, res);
    return res;
}