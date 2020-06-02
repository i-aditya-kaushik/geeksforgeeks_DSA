void myfunc(Node* root, vector<int>& res){
    if(root){
        res.push_back(root->data);
        myfunc(root->left,res);
        myfunc(root->right,res);
    }
}

bool findPair(Node* root, int sum) {
    vector<int> res;
    myfunc(root,res);
    for(int x: res){
        if(find(res.begin(),res.end(),sum-x)!=res.end() and (sum-x)!=x){
            return(1);
        }
    }
    return(0);
}
