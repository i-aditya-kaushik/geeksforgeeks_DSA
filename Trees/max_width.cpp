int getMaxWidth(Node* root)
{
    int res = 0,m;
    if(root==NULL){
        return(0);
    }
    queue<Node*> s;
    s.push(root);
    while(s.size()!=0){
        m = 0;
        int si = s.size();
        while(si!=0){
            if(s.front()->left){
                s.push(s.front()->left);
            }
            if(s.front()->right){
                s.push(s.front()->right);
            }
            m+=1;
            res = max(res,m);
            s.pop();
            si--;
        }
    }
    return(res);
}
